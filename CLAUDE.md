# BIT · öğrenci sitesi deposu

Temel Bilgi Teknolojileri (BIT) dersinin öğrenci sitesi (Quarto). Planlama belgeleri ve öğretim görevlisi materyalleri kardeş özel depodadır: `../bit-ins`.

Çalışmaya başlamadan önce oku:

1. `../bit-ins/planlama/00_proje-rehberi.md`: bütün tasarım, standart ve teknik kararlar
2. `../bit-ins/planlama/03_durum.md`: nerede kalındığı ve sıradaki işler
3. Bu deponun `README.md` dosyası: yazım kuralları (kutular, görev kartı, test sözdizimi) ve yeni hafta yayımlama listesi

Temel kurallar:

- Dil Türkçe. Hafta 1 notu (`docs/01_teknoloji-neyi-cozer.qmd`) kalıptır.
- Bu depo herkese açık bir siteyi besler (https://bit.zurrani.com; Cloudflare Pages, `main`'e her push yayını günceller): sınav soruları, cevap anahtarları ve lisansı belirsiz görseller buraya konmaz.
- Önizleme `quarto preview`, derleme `quarto render`; `_site/` depoya girmez.
- zurrani.com DNS'i Cloudflare'de (2026-10-16'dan beri); DNS değişiklikleri Cloudflare'de yapılır, WordPress DNS sayfası etkisiz. Altyapı: `ALTYAPI.md`.
