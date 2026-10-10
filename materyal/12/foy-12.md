# Hafta 12 föyü · Veriden karara

**Başlangıç dosyası:** `cihaz-arizalari-temiz.xlsx` (bu klasörde). Kayıtlar **kurgusaldır**; Hafta 11'de temizlediğin verinin temiz sürümüdür.
**Süre:** yaklaşık 60–70 dakika. Sınıfta başlarsın, öğretim görevlisinin duyurduğu tarihe kadar (bir hafta) tamamlarsın.
**Ağırlık:** Hafta 10–12'deki üç föy birlikte final notunun %20'sidir; bu föy 15 puan üzerinden değerlendirilir.
**Program:** Masaüstü Excel ya da ücretsiz LibreOffice Calc. ÇAPRAZARA işlevi yoksa DÜŞEYARA kullan (aşağıda).

Laboratuvarların sorumlusu senden kısa bir analiz istiyor: "Önümüzdeki dönem yedek parça ve bakım bütçesini nereye ayıralım?" Elinde Eylül–Kasım 2026'nın 120 arıza kaydı ve bir cihaz envanteri var. Bu föyde ders notundaki dört adımı uygulayacaksın: soru, hesap, görsel, yorum. Menü adları Türkçe Excel'e göredir; işlevlerde bağımsız değişkenler noktalı virgülle ayrılır.

## 0. Hazırlık

- Dosyayı kendi klasörüne kopyala ve adlandır: `YYYY-AA-GG_ad-soyad_foy-12.xlsx`.
- `Not` sayfasını oku. `Kayitlar` sayfasındaki verinin bir tablo nesnesi olduğuna dikkat et (adı `Arizalar`).
- `Analiz`, `Test` ve `Yorum` adında üç boş sayfa ekle.

## 1. Soru

`Analiz` sayfasının en üstüne, bu analizin cevaplayacağı soruyu bir cümleyle yaz. Ardından aşağıdaki hesapların her birinin bu soruya nasıl katkı sağlayacağını düşünerek ilerle.

## 2. Cihaz türüne göre özet (formüllerle)

`Analiz` sayfasında A sütununa beş cihaz türünü alt alta yaz (A3:A7): Bilgisayar, Projeksiyon, Yazıcı, 3B yazıcı, Osiloskop. A8'e "Toplam" yaz. B2:E2'ye başlıkları yaz: `Arıza sayısı`, `Pay`, `Ortalama süre (saat)`, `Ortanca süre (saat)`.

- **B3:** `=EĞERSAY(Kayitlar!$E$2:$E$121; A3)` yaz ve B7'ye kadar aşağı kopyala. Neden aralıkta $ var, A3'te yok? Cevabını hücrenin yanına bir notla yaz.
- **B8:** `=TOPLA(B3:B7)`. Sonuç 120 olmalı; değilse bir yazım farkı vardır.
- **C3:** `=B3/$B$8` yaz, aşağı kopyala ve yüzde biçimi ver. C8'de payların toplamı %100 olmalı.
- **D3:** `=YUVARLA(EĞERORTALAMA(Kayitlar!$E$2:$E$121; A3; Kayitlar!$J$2:$J$121); 1)`; aşağı kopyala.
- **E sütunu:** Ortanca için koşullu bir işlev yok. Bu sütunu bir sonraki adımda özet tablodan ya da filtreyle bulacaksın; şimdilik yalnızca bütün verinin değerlerini hesapla: Bir kenara `=ORTALAMA(Kayitlar!J2:J121)` ve `=ORTANCA(Kayitlar!J2:J121)` yaz. İki sayı neden bu kadar farklı? Bir cümleyle yanına yaz.

## 3. Yeni sütunlar (mantık ve arama)

`Kayitlar` tablosunun sağına iki sütun ekle. Tablo nesnesinde bir hücreye yazdığın formül bütün sütuna kendiliğinden uygulanır.

- **K sütunu, `Gecikme`:** Süre boşsa "Bekliyor", 48 saatten uzunsa "Gecikti", değilse "Zamanında" yazsın.
  `=EĞER(J2=""; "Bekliyor"; EĞER(J2>48; "Gecikti"; "Zamanında"))`
- **L sütunu, `Alım yılı`:** Cihazın alım yılını `Cihazlar` sayfasından getir.
  `=ÇAPRAZARA(F2; Cihazlar!$A$2:$A$37; Cihazlar!$D$2:$D$37)`
  ÇAPRAZARA yoksa: `=DÜŞEYARA(F2; Cihazlar!$A$2:$D$37; 4; YANLIŞ)`. Sondaki YANLIŞ'ı unutma.
- `Analiz` sayfasında: Kaç kayıt "Gecikti"? (EĞERSAY) LAB-2'de kaç "Yüksek" öncelikli arıza var? (ÇOKEĞERSAY)
- Bir hata dene: L2'deki formülde `$` işaretlerini silip formülü aşağı kopyala, sonra geri al. Ne oldu? `Test` sayfasına bir cümleyle yaz.

## 4. Özet tablo

- `Kayitlar` tablosunun içine tıklayıp **Ekle > Özet Tablo** de; yeni bir sayfaya yerleştir ve sayfanın adını `Ozet` yap.
- **Satırlar:** Laboratuvar; **Sütunlar:** Ay; **Değerler:** Kayıt No (Say). Hangi laboratuvar hangi ayda en çok arıza bildirmiş?
- Aynı sayfaya ikinci bir özet tablo kur: **Satırlar:** Cihaz türü; **Değerler:** Çözüm süresi (saat), **Değer Alanı Ayarları** ile önce Ortalama, sonra Toplam. 2. adımdaki EĞERORTALAMA sonuçlarıyla karşılaştır; aynı olmalı.
- İsteğe bağlı: Özet tabloyu "Alım yılı"na göre grupla. Eski cihazlarda arızalar daha mı uzun sürüyor? Bu bir ilişki mi, bir neden mi?

## 5. Grafikler

- **Grafik 1:** `Analiz` sayfasındaki cihaz türü ve arıza sayısı tablosundan bir **çubuk grafik** çiz. Çubukları büyükten küçüğe sırala (veriyi sıralayarak), dikey eksen sıfırdan başlasın, eksen başlığı "Arıza sayısı" olsun. Grafik başlığını bir **mesaj başlığı** yap: Grafiğin söylediğini bir cümleyle yaz.
- **Grafik 2:** `Yaniltici` sayfasındaki grafiği düzelt. Grafiğin üç sorunu var; bul ve düzelt:
  1. Dikey ekseni sıfırdan başlat (eksene sağ tık > **Ekseni Biçimlendir > En Küçük: 0**).
  2. Kasım verisi ayın yalnızca 1–19. günlerini kapsıyor. Kategori adını "Kasım (1–19)" yap ya da Kasım'ı grafikten çıkar ve bunu bir notla belirt.
  3. Başlığı veriye uygun, dürüst bir mesaj başlığıyla değiştir ve eksene başlık ekle.
- İki grafiğe de alternatif metin ekle (Hafta 10).

## 6. YZ'nin formülünü sına

- Bir YZ asistanına şu isteği yaz: "Türkçe Excel'de, Kayitlar sayfasında H sütunu 'Yüksek' olan ve J sütunu 48'den büyük olan kayıtları sayan bir formül yaz." YZ kullanmak istemiyorsan formülü kendin yaz.
- `Test` sayfasına şu tabloyu kur ve doldur:

| Test | Beklenen sonuç (elle) | Formülün sonucu | Geçti mi? |
|---|---|---|---|
| Filtreyle Yüksek ve 48'den büyük kayıtları say | | | |
| Tam 48 saat süren Yüksek öncelikli kayıtlar formüle giriyor mu? (Soru "48'den büyük" diyor) | | | |
| Süresi boş olan kayıtlar sonucu etkiliyor mu? | | | |

- Formül `>` yerine `>=` kullanıyorsa ya da İngilizce işlev adı ve virgül içeriyorsa düzelt ve neyi düzelttiğini yaz.
- YZ kullandıysan sayfanın altına Hafta 6 şablonuyla beyan ekle.

## 7. Yorum

`Yorum` sayfasına laboratuvar sorumlusuna yazılmış **en fazla dört cümlelik** bir yorum yaz. Her cümle bir bulgu, onu destekleyen bir sayı ve bir anlam içersin. Yorumunda şunlara dikkat et:

- Kasım'ın eksik olduğunu hesaba kat.
- Süre için ortalamayı mı ortancayı mı kullandığını söyle.
- Bir ilişkiyi neden gibi sunma.
- Bir öneriyle bitir: Bütçe öncelikle nereye ayrılmalı?

## Teslim

Tek dosya: `YYYY-AA-GG_ad-soyad_foy-12.xlsx` (`Kayitlar`, `Yaniltici`, `Analiz`, `Ozet`, `Test`, `Yorum` sayfalarıyla). Formüller formül olarak kalmalı; değerleri elle yazma.

## Kontrol listesi

- [ ] `Analiz` sayfasında soru, beş türün sayısı (toplam 120), payı (toplam %100) ve ortalama süresi formülle
- [ ] Mutlak ve göreli başvurunun neden öyle kullanıldığı not olarak yazılı
- [ ] Bütün veri için ortalama ve ortanca; farkın açıklaması
- [ ] `Gecikme` ve `Alım yılı` sütunları formülle; hata değeri yok
- [ ] "Gecikti" sayısı ve LAB-2'deki Yüksek öncelikli arıza sayısı formülle
- [ ] `Ozet` sayfasında iki özet tablo; sonuçlar formüllerle uyumlu
- [ ] Grafik 1: sıralı çubuklar, sıfırdan başlayan eksen, eksen başlığı, mesaj başlığı
- [ ] Grafik 2: eksen, eksik dönem ve başlık düzeltildi
- [ ] İki grafikte alternatif metin
- [ ] `Test` sayfasında üç test ve sonuçları; YZ kullanıldıysa beyan
- [ ] `Yorum` sayfasında bulgu, sayı ve anlam içeren en fazla dört cümle ve bir öneri
