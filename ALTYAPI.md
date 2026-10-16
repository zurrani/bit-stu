# bit-stu · Altyapı ve yayın

**Son güncelleme:** 16 Ekim 2026 (zurrani.com DNS'inin Cloudflare'e taşınmasından sonraki denetim). Öğrenci sitesinin nerede ve nasıl yayımlandığının tek kaydı budur; `README.md` ve `../bit-ins/planlama/00_proje-rehberi.md` (4.8) buraya gönderme yapar. Bu dosya sitede yayımlanmaz (`_quarto.yml` render listesinde yok).

Parola, belirteç ya da API anahtarı bu depoda yoktur ve buraya yazılmaz. Yayın bir belirteç kullanmaz: Pages projesi GitHub'a Cloudflare'in GitHub uygulamasıyla bağlıdır. Cloudflare, GitHub ve WordPress.com hesaplarına öğretim görevlisi kendi hesabıyla girer.

## Özet

| Konu | Değer |
|---|---|
| Adres | **https://bit.zurrani.com**: öğrencilere verilen tek adres |
| Pages projesi | `bit-stu` (Cloudflare hesabı "Zurrani@gmail.com's Account"); GitHub `zurrani/bit-stu`; production branch `main` |
| Pages adresi | `https://bit-stu.pages.dev`. 16 Ekim 2026'da Türkiye'deki bir ağdan açılmadı (bağlantı şifreli oturum kurulurken kesildi); öğrencilere verilmez |
| DNS'in yeri | **Cloudflare**, bölge `zurrani.com` (Free plan); ad sunucuları `alan.ns.cloudflare.com`, `priscilla.ns.cloudflare.com`; 16 Ekim 2026'dan beri. WordPress.com'daki DNS kayıtları kullanılmaz |
| Kayıt | CNAME `bit` → `bit-stu.pages.dev`, **Proxied** (turuncu bulut) |
| Pages özel alan adı | `bit.zurrani.com` (Pages → bit-stu → Custom domains) |
| Sertifika | Cloudflare (Google Trust Services); kendiliğinden yenilenir. 16 Ekim 2026'daki sertifikanın bitişi 9 Ocak 2027 |
| Alan adı kaydı ve yenileme | **WordPress.com**; yenileme 22 Aralık 2026, otomatik. Yenileme olmazsa site de kapanır |
| Blog ve öbür projeler | `zurrani.com` ve `www` WordPress.com'da (DNS only). Aynı bölgede, aynı kalıpla: `part66edu`, `part66sim`, `matsim` ve başka projeler |
| Joker kayıt | `*` → `zurrani.com`, DNS only. Yanlış yazılan bir alt ad `http://`'de bloga gider, `https://`'te tarayıcı sertifika uyarısı verir (WordPress'in o ad için sertifikası yok) |
| Web Analytics | Pages projesinde açık; çerezsiz, sayfa başına bir ölçüm betiği. Ziyaretçiye açıklaması: `hakkinda.qmd` |

## Derleme ayarları (Cloudflare → Workers & Pages → bit-stu → Settings)

| Ayar | Değer |
|---|---|
| Production branch | `main` |
| Framework preset | None |
| Build command | aşağıdaki satır |
| Build output directory | `_site` |

```text
mkdir -p /tmp/q && curl -sL https://github.com/quarto-dev/quarto-cli/releases/download/v1.10.19/quarto-1.10.19-linux-amd64.tar.gz | tar xz -C /tmp/q && /tmp/q/quarto-1.10.19/bin/quarto render
```

Quarto sürümü yerelde güncellenirse derleme komutundaki sürüm de güncellenir. Yayımlanan profil öntanımlı (havacılık katmanlı) profildir.

## Bölge ayarları (16 Ekim 2026)

Bölge ayarları `zurrani.com`'daki bütün Proxied kayıtları etkiler; tek bir sitede değiştirilmez.

| Ayar | Durum | Bu siteye etkisi |
|---|---|---|
| Browser Cache TTL | Öntanımlı (4 saat) | Sayfalar `max-age=0` ile gelir, güncellemeler hemen görünür. Önbelleklenebilir dosyalar (`materyal/` altındaki docx, xlsx, pptx; görseller, yazı tipleri, `robots.txt`) 4 saatlik tarayıcı önbelleğiyle gelir: aynı adla güncellenen bir dosya 4 saate kadar eski görünebilir. Açık karar: "Respect Existing Headers" (`03_durum.md`) |
| Yapay zekâ botları (Search, Agent, Training) | Allow; Bot Preference Sync kapalı | Engel yok |
| DNSSEC | Kapalı | Etki yok |
| E-posta (MX) | Yok | Etki yok |

## Sitenin davranışı

- `_headers`, `_redirects`, form, giriş, API ve WebSocket yok; site statik. Arama ve Kendini sına tarayıcıda çalışır.
- Dışarıya giden tek istek Cloudflare Web Analytics betiği. Yazı tipleri yerelde.
- `.html` uzantılı adresler 308 ile uzantısız adrese, `http://` 301 ile `https://`'e yönlenir.
- `robots.txt` ve `sitemap.xml` dosyalarını Quarto üretir (`_quarto.yml`, `site-url`).
- 404 sayfası yok: olmayan bir adres 200 ile ana sayfayı döndürür (Pages, `404.html` bulamayınca böyle davranır). Açık iş: `03_durum.md`, Sıradakiler.

## Yeni bir alt alan adı eklemek

DNS değişiklikleri yalnızca **Cloudflare → zurrani.com → DNS → Records**'ta yapılır; WordPress.com'un DNS sayfası etkisizdir.

1. Pages projesi hazırsa en kısa yol: Workers & Pages → proje → Custom domains → Set up a custom domain → `<ad>.zurrani.com`. Bölge aynı hesapta olduğu için Cloudflare CNAME kaydını (Proxied) kendisi ekler.
2. Kaydı elle eklemek gerekirse: DNS → Records → Add record → CNAME, ad `<ad>`, hedef `<proje>.pages.dev`, Proxied. Ardından aynı adı Pages projesinin Custom domains bölümüne de ekle; eklenmezse site hata verir.
3. Birkaç dakika sonra aşağıdaki sağlık denetimini o adla çalıştır.

## Sağlık denetimi

Salt okunur; hiçbir ayarı değiştirmez. Komut: `KOMUTLAR.md` (proje kök klasörü), bölüm 7, "Canlı site". Beklenen sonuç:

- Ad sunucuları `alan` ve `priscilla`.
- Sayfalar 200, her satırda `cf-ray` dolu (Cloudflare'den geçiyor), `cache: DYNAMIC`, `max-age=0, must-revalidate`.
- `.html` uzantılı adres 308, `konum` uzantısız adres; `http://` 301, `konum` `https://`.
- docx: 200 (`cache` MISS ya da HIT).
- Sertifika `CN=bit.zurrani.com`, `gecerli: True`, bitiş tarihi geçmemiş.
- Ölçüm betiği 1 (2 olursa analitik çift sayıyor).

Bir ayarı değiştirdikten sonra kod değişmeden yeniden yayımlamak: `KOMUTLAR.md`, bölüm 7.

## Değişiklik geçmişi

| Tarih | Değişiklik |
|---|---|
| 11 Ekim 2026 | Yayın kuruldu (Cloudflare Pages, depo özel). DNS WordPress.com'daydı: orada CNAME `bit` → `bit-stu.pages.dev`. Karar: rehber 4.8 |
| 16 Ekim 2026 | zurrani.com DNS'i Cloudflare'e taşındı (ad sunucuları `alan`, `priscilla`); `bit` kaydı Cloudflare'e birebir kopyalandı ve Proxied yapıldı. Alan adı kaydı WordPress.com'da kaldı. Denetim: site, sertifika ve analitik doğru; yeni olarak 4 saatlik tarayıcı önbelleği (Browser Cache TTL); Pages adresi bu ağdan açılmıyor |
