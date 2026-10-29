"""Bu deponun içeriğini tek PDF kitabı yapar (bit-ins ve bit-stu'da aynı betik).

    python _web/pdf_uret.py                      bütün bölümler
    python _web/pdf_uret.py --sadece ogretim     yalnızca seçilen bölümler
    python _web/pdf_uret.py --genel              (bit-stu) havacılık kutuları çıkarılır

Dosyalar geçici bir klasöre kopyalanıp orada Quarto + Typst ile derlenir; özgün dosyalara
dokunulmaz. PDF depodaki _pdf/ klasörüne yazılır; bu klasör git'e girmemelidir.
bit-ins çıktısı sınav soruları ve cevap anahtarları içerir: öğrenciyle paylaşılmaz.
Gereken: Quarto 1.7 ya da sonrası (Typst içinde gelir; 1.10.19 ile denendi) ve Python 3.
"""
import argparse, re, shutil, subprocess, sys, tempfile
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
CIKTI = KOK / "_pdf"
OGRENCI_SITESI = (KOK / "docs").is_dir()          # bit-stu mu, bit-ins mi


def _sirali(desen):
    return sorted(str(p.relative_to(KOK)).replace("\\", "/") for p in KOK.glob(desen))


if OGRENCI_SITESI:
    AD = "BIT · Ders notları"
    ALT = "Temel Bilgi Teknolojileri · öğrenci sitesi (bit.zurrani.com)"
    EK_SIRA = ["ekler/sozluk.qmd"] + [f for f in _sirali("ekler/*.qmd") if not f.endswith("sozluk.qmd")]
    BOLUMLER = {
        "notlar": ("Ders notları", _sirali("docs/*.qmd")),
        "ekler": ("Ekler", EK_SIRA),
        "hakkinda": ("Site", ["hakkinda.qmd"]),
    }
else:
    AD = "BIT · Öğretim görevlisi kitabı"
    ALT = "Temel Bilgi Teknolojileri"
    BOLUMLER = {
        "planlama": ("Planlama", [f"planlama/{a}.md" for a in (
            "00_proje-rehberi", "01_ders-taslagi", "02_kaynak-envanteri", "03_durum",
            "04_yeni-oturum", "05_sinav-modulu", "06_teyit-raporu", "07_yari-ters-yuz-taslak",
            "08_iyilestirme-plani", "09_icerik-olcumleri", "10_kanit-plani", "11_vaka-haritasi")]),
        "ogretim": ("Öğretim", [f"ogretim/{i:02d}_ogretim.md" for i in range(1, 15)]),
        "soru-bankasi": ("Soru bankası", ["soru-bankasi/00_standartlar.md"]
            + [f"soru-bankasi/{i:02d}_soru-bankasi.md" for i in range(1, 15)]
            + ["soru-bankasi/taslak_hafta-02-14.md"]),
        "performans-testi": ("Performans testi", ["performans-testi/performans-testi.md",
            "performans-testi/yapabilirim-listesi.md", "performans-testi/uretim/README.md"]),
        "sinav": ("Sınav modülü", ["sinav/README.md", "sinav/KAPANIS.md"]),
        "depo": ("Depo", ["README.md", "materyal-uretim/README.md"]),
    }

SAYFA = "\n```{=typst}\n#pagebreak()\n```\n"
ON_BILGI = re.compile(r"\A---\n(.*?)\n---\n", re.S)
HTML_BLOK = re.compile(r"```\{=html\}\n(.*?)\n```", re.S)


def gorev_karti_metni(html):
    """Görev kartı (HTML) PDF'te görünmez; içeriği iki satırlık düz metne çevrilir."""
    alanlar = re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", html)
    soru = re.search(r"<p class=\"gk-soru\"><b>(.*?)</b>\s*(.*?)</p>", html, re.S)
    ust = " · ".join(f"**{k}:** {v}" for k, v in alanlar)
    return ust + ("\n\n**" + soru.group(1) + "** " + soru.group(2).strip() if soru else "")


def hazirla(metin, genel):
    baslik = alt = None
    m = ON_BILGI.match(metin)
    if m:
        for anahtar in ("title", "subtitle"):
            a = re.search(rf'^{anahtar}:\s*"?(.*?)"?\s*$', m.group(1), re.M)
            if a and anahtar == "title":
                baslik = a.group(1)
            elif a:
                alt = a.group(1)
        metin = metin[m.end():]
    metin = HTML_BLOK.sub(
        lambda b: gorev_karti_metni(b.group(1)) if "gorev-karti" in b.group(1) else "", metin)

    cikti, kapali, atla = [], False, False
    if baslik:
        cikti.append(f"# {alt + ' · ' if alt else ''}{baslik}")
    for satir in metin.split("\n"):
        if satir.lstrip().startswith("```"):
            kapali = not kapali
        if not kapali:
            if genel and re.match(r"^:::\s*\{.*kutu-havacilik", satir):
                atla = True
                continue
            if atla:
                atla = not re.match(r"^:::\s*$", satir)
                continue
            k = re.match(r"^:::+\s*\{[^}]*callout-[^}]*\}\s*$", satir)
            if k:
                # Typst'in kutu simgeleri internetten paket indirir; çevrimdışı da çalışsın diye
                # kutu, kalın başlıklı düz bir bloğa çevrilir.
                ad = re.search(r'title="([^"]*)"', satir)
                cikti.append("::: {.kutu}")
                if ad:
                    cikti += ["", f"**{ad.group(1)}**", ""]
                continue
            if re.match(r"^---+\s*$", satir):
                satir = "***"        # yatay çizgi: iki "---" arası YAML sanılmasın
            if re.match(r"^#{1,5} ", satir):
                satir = "#" + satir                      # başlıklar bir düzey aşağı
            satir = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", satir)          # sayfa içi bağlantı
            satir = re.sub(r"\[([^\]]+)\]\((?!https?:)[^)]*\.(?:qmd|md)[^)]*\)", r"\1", satir)
        cikti.append(satir)
    return "\n".join(cikti)


def main():
    ap = argparse.ArgumentParser(description="Depoyu tek PDF kitabı yap.")
    ap.add_argument("--sadece", nargs="+", choices=list(BOLUMLER), help="yalnızca bu bölümler")
    ap.add_argument("--genel", action="store_true", help="havacılık kutularını çıkar")
    ap.add_argument("--ad", default=KOK.name, help="PDF dosya adı (uzantısız)")
    a = ap.parse_args()

    # Geçici klasör OneDrive dışında: eşitleme dosyaları kilitleyip silmeyi engellemesin.
    gecici = Path(tempfile.mkdtemp(prefix="bit_pdf_"))
    try:
        parcalar = ["---", f'title: "{AD}"', f'subtitle: "{ALT}"', 'author: "Öğr. Gör. Emre Akar"',
                    "lang: tr", "format:", "  typst:", "    toc: true", "    toc-depth: 2",
                    "    number-sections: false", "    papersize: a4", "    fontsize: 10pt",
                    "    margin: { x: 1.8cm, y: 2cm }",
                    "    from: markdown-tex_math_dollars-fancy_lists", "---", ""]
        for anahtar in (a.sadece or list(BOLUMLER)):
            ad, dosyalar = BOLUMLER[anahtar]
            parcalar += [SAYFA, f"# {ad}", ""]
            for f in dosyalar:
                parcalar += [SAYFA, hazirla((KOK / f).read_text(encoding="utf-8"), a.genel), ""]
        (gecici / "kitap.qmd").write_text("\n".join(parcalar), encoding="utf-8")

        r = subprocess.run(["quarto", "render", "kitap.qmd", "--to", "typst"], cwd=gecici)
        if r.returncode:
            sys.exit("Derleme hatası: yukarıdaki iletiye bakın.")
        CIKTI.mkdir(exist_ok=True)
        hedef = CIKTI / f"{a.ad}{'-genel' if a.genel else ''}.pdf"
        shutil.copyfile(gecici / "kitap.pdf", hedef)
        print(f"PDF hazır: {hedef} ({hedef.stat().st_size // 1024} KB)")
    finally:
        shutil.rmtree(gecici, ignore_errors=True)


if __name__ == "__main__":
    main()
