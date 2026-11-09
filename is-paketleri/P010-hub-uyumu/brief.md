# P010 · Hub uyumu ve bayat bilgi (hub K-010, K-046)
Açan: Claude Code (dev-hub) · Tarih: 2026-11-09 · Alan ajan: Antigravity (komut satırı, yazma kipi) · Durum: açık
Model: gemini-4-argon-high · Düzey: yüksek · Neden: bilgi kaybetmeden düzeltme; her değişiklik kanıta dayanmalı.
Dal: `hub-uyumu` (lider açtı; commit ve push liderindir). Yayın düzeni: `push`.

## Kanon
Önce `C:\dev\_hub\ortak\KURALLAR.md` (Hub uyumu: K-010 atıf satırı, K-046 belge hijyeni) ve bu projenin kural dosyası. Bulgular ve kanıtlar: `C:\dev\_hub\is-paketleri\P001-belge-tarama-egitim\rapor.md` → "## bit-stu" bölümü (her iddiayı düzeltmeden önce yerinde yeniden doğrula; doğrulanamayanı değiştirme, rapora "şüphe" yaz).

## Görev
1. `CLAUDE.md` başına tek satır: `Ortak kurallar C:\dev\_hub\ortak\KURALLAR.md'den yüklenir; burada tekrarlanmaz.`
2. `CLAUDE.md`'deki ortak kuralların kopyaları (GitHub Actions kotası ve taslak PR düzeni, OneDrive yasağı, iki bilgisayar, MSIX/AppData yönlendirmesi, PowerShell `&&`/BOM tuzakları, şapka ve karar sunumu): projeye özgü fark ya da sıkılaştırma dışında silinir, yerine hub atfı (`ci-kotasi` skill'i gibi) kalır. Yayın satırı (`main`'e push yayını günceller) kalır.

## Çıktı
- Rapor: `is-paketleri/P010-hub-uyumu/rapor.md`. İlk satırlar künye (`Şapka`, `Ajan · Model · Düzey`, `Okunan dosyalar`, `Başlangıç` · `Bitiş`).
- Tablo: dosya:eski satır · ne yapıldı (silindi / düzeltildi / atfa indi / eklendi) · neden · kanıt.
- "Lidere öneriler" (kilit dışı gerekenler).
- Son satır: `Durum: bitti`

## Kilit
- Yazabileceğin dosyalar: `CLAUDE.md` ve bu paket klasörü.
- Başka dosya değiştirme, taşıma ya da silme yok.

## Dokunulmayacaklar
- Kod ve içerik dosyaları, build çıktıları, `.github/`.
- Git'te yazma yok (yalnız `status`, `log`, `diff`, `show`). Gizli dosyalar (`.env*`, `*.keystore`, `keystore.properties`, `Private/`, `C:\dev\_keys`, adında `key`/`token` geçen dosyalar) okunmaz.

## Bitiş ölçütü
- Kural dosyasının başında hub atıf satırı (görevde varsa); silinen her ortak kural kopyasının hub'da karşılığı var; projeye özgü hiçbir kural kaybolmadı.
- Kontrol komutu: lider çalıştırır; sen yalnız okuma amaçlı (görevde izin verilenleri) çalıştırabilirsin.
