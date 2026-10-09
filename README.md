# BIT · Temel Bilgi Teknolojileri (öğrenci sitesi)

Temel Bilgi Teknolojileri (Basic Information Technologies) dersinin öğrenciye açık içeriği: ders notları, ekler, sözlük ve web sunumları. Site [Quarto](https://quarto.org) ile derlenir.

Öğretim görevlisi materyalleri (ders akışları, soru bankası, performans testi) bu depoda **yoktur**; özel `bit-ins` deposundadır.

Planlanan yayın adresi: `https://bit.zurrani.com` (`_quarto.yml` içindeki `site-url` ile değiştirilebilir).

## Klasör yapısı

```
bit-stu/
├─ _quarto.yml            site ayarları: menü, tema, Türkçe arayüz metinleri
├─ _quarto-genel.yml      havacılık kutuları olmadan derleme profili
├─ index.qmd              ana sayfa
├─ hakkinda.qmd           ders, yazar, gizlilik, YZ beyanı, lisans
├─ docs/                  ders notları: 00_cerceve.qmd, 01_…, 02_… 14_…
├─ ekler/                 sözlük ve ekler (A, B, C)
├─ slides/                web sunumları (sıradaki aşama)
├─ materyal/              öğrencinin indireceği dosyalar, haftaya göre alt klasörler
└─ assets/
   ├─ css/                bit.scss (açık tema), bit-dark.scss, fonts.css, genel.css
   ├─ js/quiz.html        "Kendini sına" bileşeni
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

**Görev kartı:** Her haftanın başında, `docs/01_teknoloji-neyi-cozer.qmd` dosyasındaki HTML bloğu kopyalanıp alanları güncellenir.

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
- [ ] `_quarto.yml` içinde kenar çubuğuna hafta eklendi
- [ ] `index.qmd` içindeki listede hafta "Yayında" yapıldı ve bağlantı eklendi
- [ ] `quarto preview` ile açık ve karanlık temada, telefonda kontrol edildi

## Yayın

**Karar (9 Ekim 2026):** Bu depo herkese açık yapılacak ve site GitHub Pages ile yayımlanacak:

```bash
quarto publish gh-pages
```

`bit.zurrani.com` alt alan adı bir DNS (CNAME) kaydıyla bağlanır. Depo herkese açık olacağı için buraya yalnızca öğrenciye açık içerik girer: sınav soruları, lisansı belirsiz görseller ve kişisel veri hiçbir zaman konmaz. Kurulum adımları uygulandığında bu bölüm güncellenecek.

## İlk gönderim

```bash
git init
git add .
git commit -m "BIT öğrenci sitesi: iskelet ve Hafta 1"
git branch -M main
git remote add origin https://github.com/zurrani/bit-stu.git
git push -u origin main
```

## Lisans

Metin içeriği [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.tr) ile paylaşılır (`LICENSE`). Yazı tipleri SIL Open Font License ile dağıtılır (`assets/fonts/`).
