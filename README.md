# BIT · Temel Bilgi Teknolojileri (öğrenci sitesi)

Temel Bilgi Teknolojileri (Basic Information Technologies) dersinin öğrenciye açık içeriği: ders notları, ekler, sözlük ve web sunumları. Site [Quarto](https://quarto.org) ile derlenir.

Öğretim görevlisi materyalleri (ders akışları, soru bankası, performans testi) bu depoda **yoktur**; özel `bit-ins` deposundadır.

Yayın adresi: **https://bit.zurrani.com** (Cloudflare Pages; `main` dalına her push siteyi kendiliğinden günceller).

## Klasör yapısı

```
bit-stu/
├─ _quarto.yml            site ayarları: menü, tema, Türkçe arayüz metinleri
├─ _quarto-genel.yml      havacılık kutuları olmadan derleme profili
├─ index.qmd              ana sayfa
├─ hakkinda.qmd           ders, yazar, gizlilik, YZ beyanı, lisans
├─ docs/                  ders notları: 00_cerceve.qmd, 01_…, 02_… 14_…
├─ ekler/                 sözlük ve ekler (A, B, C, D, E: ders izlencesi, F: DigComp 3.0)
├─ slides/                web sunumları (sıradaki aşama)
├─ materyal/              öğrencinin indireceği dosyalar, haftaya göre alt klasörler
└─ assets/
   ├─ css/                bit.scss (açık tema), bit-dark.scss, fonts.css, mobil.css, genel.css
   ├─ js/quiz.html        "Kendini sına" bileşeni
   ├─ js/gorunum.html     üst çubukta metin boyutu (beş kademe) ve tam ekran düğmeleri
   ├─ fonts/              yerel yazı tipleri (OFL lisanslı)
   └─ img/                görseller, haftaya göre alt klasörler
```

## Çalışma akışı

1. [Quarto'yu](https://quarto.org/docs/get-started/) kur (Windows için tek kurulum dosyası).
2. Klasörde `quarto preview` çalıştır; site tarayıcıda açılır, kaydettikçe yenilenir.
3. Yayına hazırlarken `quarto render` çalıştır; çıktı `_site/` klasörüne yazılır (depoya girmez).
4. Havacılık kutuları olmayan genel sürüm için: `quarto render --profile genel`.

Dosyalar düz Markdown'dır; VS Code, Positron ya da herhangi bir metin düzenleyiciyle düzenlenebilir.

## İçerik yazım kuralları

**Dosya adı:** `docs/NN_kisa-baslik.qmd` (iki haneli hafta numarası, Türkçe karaktersiz, tireli).

**Kutular:**

```markdown
::: {.callout-important .kutu-efsane title="Efsane mi gerçek mi?"}
:::
::: {.callout-note .kutu-havacilik title="Havacılık bağlantısı"}
:::
::: {.callout-tip .kutu-fayda title="Bu ne işime yarar?"}
:::
::: {.callout-caution .kutu-dusun title="Düşün"}
:::
::: {.callout-note .kutu-izle appearance="simple" title="İzle"}
:::
```

Programa özgü örnekler yalnızca `.kutu-havacilik` kutularında yer alır; ana metin genel kalır.

**Görev kartı:** Her haftanın başında, `docs/01_teknoloji-neyi-cozer.qmd` dosyasındaki HTML bloğu kopyalanıp alanları güncellenir. Okuma süresi ve kelime sayısı elle yazılmaz: not değişince `bit-ins` klasöründe `python _web/olcum.py --belge --yaz` çalıştırılır.

**Kendini sına:** Seçeneklerdeki parantez ters eğik çizgiyle yazılır (`A\)`), yoksa Markdown onu ayrı bir liste sanar.

```markdown
::: {.quiz-q data-answer="B" data-explain="Kısa gerekçe."}
**1.** Soru kökü?

- A\) …
- B\) …
:::
```

Yalnızca öğrenmeyi destekleyen sorular buraya girer; sınav soruları hiçbir zaman bu depoya girmez.

**Görseller:** Bu depo herkese açık yayımlanan bir siteyi besler. Yalnızca kendi ürettiğin, kamu malı ya da açık lisanslı görseller konur ve lisansı yanına yazılır. Film kareleri ve stok görseller `bit-ins` deposunda kalır.

## Yeni bir haftayı yayımlama

- [ ] `docs/NN_….qmd` dosyası Hafta 1 standardına uygun (görev kartı, çıktılar, kutular, Akılda kalsın, Kendini sına)
- [ ] Yeni kavramlar `ekler/sozluk.qmd` dosyasına eklendi
- [ ] `_quarto.yml` içinde kenar çubuğuna ve üst menüdeki "Ders notları" açılır listesine hafta eklendi
- [ ] `index.qmd` içindeki listede hafta "Yayında" yapıldı ve bağlantı eklendi
- [ ] `quarto preview` ile açık ve karanlık temada, telefonda kontrol edildi

## Yayın

Site **Cloudflare Pages** ile yayımlanır; depo özel kalır, yalnızca derlenmiş site (`_site/`) açılır. Adres `https://bit.zurrani.com` (yedek adres `https://bit-stu.pages.dev`). Karar ve gerekçe: `bit-ins/planlama/00_proje-rehberi.md`, 4.8.

> **Düzeltme (16 Ekim 2026):** zurrani.com'un DNS'i Cloudflare'e taşındı. Yedek adres `bit-stu.pages.dev` Türkiye'deki bir ağdan açılmadı; öğrencilere yalnızca `bit.zurrani.com` verilir. Cloudflare ayarları, DNS, derleme komutu ve sağlık denetimi artık tek yerde: [`ALTYAPI.md`](ALTYAPI.md).

**Güncelleme:** Bir notu değiştir, yerelde `quarto preview` ile kontrol et, sonra:

```bash
git add .
git commit -m "..."
git push
```

Cloudflare `main` dalındaki her push'ta siteyi kendisi derler (yaklaşık bir dakika). Durumu Cloudflare panelinde bit-stu → Deployments sekmesinde görürsün. Bir derleme başarısız olursa yayındaki site değişmez; günlüğe "Details"ten bakılır.

Cloudflare'deki ayarlar (Pages projesi, özel alan adı, DNS kaydı, derleme komutu) ve sağlık denetimi: [`ALTYAPI.md`](ALTYAPI.md). Tablonun 16 Ekim 2026'ya kadarki hâli orada, "Değişiklik geçmişi"nde (özel alan adı satırı: "WordPress.com DNS'inde CNAME `bit` → `bit-stu.pages.dev`").

Quarto sürümü yerelde güncellenirse `ALTYAPI.md`'deki derleme komutundaki sürüm de güncellenir. Yayımlanan profil öntanımlı (havacılık katmanlı) profildir; genel profil yalnızca yerelde derlenir.

Depo özel olsa da site herkese açıktır: buraya yalnızca öğrenciye açık içerik girer. Sınav soruları, lisansı belirsiz görseller ve kişisel veri hiçbir zaman konmaz. `$` işaretini (örneğin `$B$7`) ters tırnak içinde yaz; yoksa Quarto onu matematik formülü sanar ve sayfa dışarıdan MathJax yükler.

## Lisans

Metin içeriği [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.tr) ile paylaşılır (`LICENSE`). Yazı tipleri SIL Open Font License ile dağıtılır (`assets/fonts/`).
