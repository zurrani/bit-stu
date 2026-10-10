# Hafta 11 föyü · Kirli tabloyu temizle

**Başlangıç dosyası:** `cihaz-arizalari.xlsx` (bu klasörde). Kayıtlar **kurgusaldır**.
**Süre:** yaklaşık 60 dakika. Sınıfta başlarsın, öğretim görevlisinin duyurduğu tarihe kadar (bir hafta) tamamlarsın.
**Ağırlık:** Hafta 10–12'deki üç föy birlikte final notunun %20'sidir; bu föy 15 puan üzerinden değerlendirilir.
**Program:** Masaüstü Excel ya da ücretsiz LibreOffice Calc. Google E-Tablolar'da da yapılabilir, ama bazı menü adları farklıdır.

Bir kampüsteki laboratuvar görevlileri cihaz arızalarını üç ay boyunca bir tabloya yazmış. Herkes kendi alışkanlığıyla yazdığı için tablo bir analize hazır değil: Aynı cihaz türü beş farklı biçimde yazılmış, tarihlerin bir kısmı metin, bazı bilgiler yalnızca renkle tutulmuş. Gelecek hafta bu verinin temiz sürümüyle analiz yapacaksın. Bu hafta senin görevin tabloyu **düzenli veriye** dönüştürmek ve bunu yaparken ne yaptığını kaydetmek. Menü adları Excel'e göredir; bulamazsan programın arama kutusuna işlevin adını yaz.

## 0. Hazırlık: orijinali koru

- Dosyayı kendi klasörüne kopyala ve adlandır: `YYYY-AA-GG_ad-soyad_foy-11.xlsx`.
- `Kayitlar` sayfasının adını `Ham` yap. Sayfa sekmesine sağ tıklayıp **Taşı veya Kopyala > Kopya oluştur** ile bir kopyasını al ve kopyanın adını `Temiz` yap. **Bütün çalışmayı `Temiz` sayfasında yap; `Ham` sayfasına dokunma.**
- `Gunluk` adında boş bir sayfa ekle. Yaptığın her önemli işlemi buraya bir satır olarak yazacaksın: ne yaptın, kaç kaydı etkiledi.

## 1. Tanı: önce sorunları bul

- Başlık satırına (3. satır) tıklayıp **Veri > Filtre**'yi aç. Her sütunun okunu açıp oradaki farklı değerlerin listesine bak.
- Seçtiğin hücrelerin değerini **formül çubuğunda** kontrol et. Sola yaslanmış sayılara ve tarihlere dikkat et.
- `Gunluk` sayfasına bulduğun sorun türlerini yaz. En az sekiz farklı sorun türü var.

## 2. Yapıyı düzelt

- Birleştirilmiş başlık satırını ve altındaki boş satırı sil; sütun adları 1. satırda olsun.
- Eylül'ün sonundaki "EYLÜL TOPLAMI" satırını ve tablonun en altındaki not satırını sil. Notun içeriğini günlüğe taşı.
- "Durum" sütununda bazı hücreler boş ama yeşile boyanmış; tablonun altındaki nota göre yeşil "çözüldü" demek. Bilgiyi renkten yazıya taşı: **Filtre > Renge Göre Filtrele** ile yeşil hücreleri seç ve hepsine "Çözüldü" yaz. Sonra hücrelerin dolgu rengini kaldır. Sarı hücrelerde zaten "Parça bekliyor" yazıyor; onların da rengini kaldır.

## 3. Birleşik sütunu böl

- "Laboratuvar / Cihaz türü" sütununun sağına boş bir sütun ekle.
- Sütunu seçip **Veri > Metni Sütunlara Dönüştür** de: "Sınırlandırılmış", ayraç olarak **Diğer: /** seç.
- İki yeni sütunun adı `Laboratuvar` ve `Cihaz türü` olsun. Bölünen değerlerin başında ya da sonunda boşluk kaldı; bir yardımcı sütunda `=KIRP(…)` ile temizle, sonucu **Özel Yapıştır > Değerler** ile yerine yapıştır ve yardımcı sütunu sil.

## 4. Yazımları standartlaştır

Hedef değerler şunlardır:

| Sütun | İzin verilen değerler |
|---|---|
| Cihaz türü | Bilgisayar, Projeksiyon, Yazıcı, 3B yazıcı, Osiloskop |
| Öncelik | Yüksek, Orta, Düşük |
| Durum | Çözüldü, Açık, Parça bekliyor |
| Cihaz kodu | İki büyük harf ya da "3D", tire ve dört rakam: `PC-0214`, `3D-0833` |

- Filtre listesinden farklı yazımları gör; **Bul ve Değiştir** (Ctrl + H) ya da filtreyle seçip düzelt. Örnek: "PC" bir cihaz türü olarak yazıldığında "Bilgisayar" demektir; "Projektör" "Projeksiyon"dur; "Y" "Yüksek", "D" "Düşük"tür.
- Cihaz kodlarında küçük harf, tire yerine boşluk ve sonda boşluk var. Bir yardımcı sütunda `BÜYÜKHARF` ve `KIRP` kullanabilir ya da **Hızlı Doldurma** (Ctrl + E) deneyebilirsin. Hızlı doldurmanın tahminini mutlaka kontrol et.
- "Arıza" ve "Öncelik" sütunlarında da sonda boşluk kalmış değerler var; KIRP'la temizle.
- Her standartlaştırmayı günlüğe yaz: hangi yazım, hangi değere, kaç kayıt.

## 5. Veri türlerini düzelt

**Tarih:** Sütunda gerçek tarihlerin yanında metin olarak yazılmış tarihler var ("04.09.2026", "7 Eylül 2026", "2026-09-07", "9/7/2026").

- Metin tarihleri gerçek tarihe çevir. Türkçe ayarda "04.09.2026" biçimindeki metinler çoğu zaman Bul ve Değiştir ile noktayı yine noktayla değiştirerek ya da **Metni Sütunlara Dönüştür > Sütun veri biçimi: Tarih (GAY)** ile tarihe döner. Diğerlerini elle düzeltebilirsin.
- "9/7/2026" gibi gün ve ayı belirsiz tarihlerde kayıt numarasına ve çevredeki kayıtlara bak: Kayıtlar tarih sırasıyla girilmiştir.
- K-033 kaydının tarihi "31.09.2026" yazılmış; böyle bir gün yok. Kayıt sorumlusu doğru tarihin **24.09.2026** olduğunu bildirdi. Düzelt ve günlüğe "kaynağına sorularak düzeltildi" diye yaz.
- Bütün sütuna `GG.AA.YYYY` biçimini ver. Kontrol: Sütunda hiçbir değer sola yaslı kalmamalı.

**Çözüm süresi:** Sütunda sayılar, metin olarak saklanmış sayılar ve "8 saat" gibi birimli değerler var.

- Bul ve Değiştir ile " saat" ifadesini sil.
- Bazı metinlerde ondalık ayırıcı olarak nokta kullanılmış ("2.5"). Türkçe ayarda ondalık ayırıcı virgüldür ve "2.5" bir sayı değil, hatta bir tarih (2 Mayıs) sanılabilir. Yalnızca bu sütunu seçip Bul ve Değiştir ile noktayı virgüle çevir.
- Metin olarak saklanan sayıları sayıya çevir (hücrenin yanındaki uyarı simgesi > **Sayıya Dönüştür**).
- Sütunun adını `Çözüm süresi (saat)` yap. Boş hücreler henüz çözülmemiş arızalardır; onlara 0 yazma.

## 6. Yinelenenleri kaldır

- **Veri > Yinelenenleri Kaldır**. Bütün sütunlar seçili kalsın. Program kaç kaydın silindiğini söyler; bu sayıyı ve silinen kayıt numaralarını günlüğe yaz.

## 7. Kontrol et ve düzenle

- **Giriş > Tablo Olarak Biçimlendir** ile veriyi bir tablo nesnesine çevir (ilk satır başlık).
- **Görünüm > Bölmeleri Dondur > Üst Satırı Dondur**.
- Tabloyu "Tarih"e göre eskiden yeniye sırala.
- **Kontrol toplamları:** Tabloda **120 kayıt** olmalı. "Çözüm süresi (saat)" sütununu seçtiğinde durum çubuğunda **Toplam 2552,2** görünmeli. Bu iki sayı tutmuyorsa bir yerde bir kayıt eksik, fazla ya da metin olarak kalmıştır; bulmak için filtreyi kullan.

## 8. Hatayı girişte durdur

- "Öncelik" ve "Durum" sütunlarına **Veri > Veri Doğrulama > Liste** ile yukarıdaki izin verilen değerlerden oluşan açılır listeler koy. Listede olmayan bir değer girildiğinde bir uyarı mesajı göster.
- "Çözüm süresi (saat)" sütununa **Giriş > Koşullu Biçimlendirme > Hücre Kurallarını Vurgula > Büyüktür** ile 48'den büyük değerleri vurgulayan bir kural ekle.
- Tablonun altına bir deneme kaydı ekle: Öncelik sütununa "yuksek" yazmayı dene ve uyarıyı gör. Sonra deneme kaydını sil.

## 9. CSV olarak dışa aktar

- `Temiz` sayfası açıkken **Dosya > Farklı Kaydet**, tür **CSV UTF-8 (virgülle ayrılmış)**. Dosya adı: `YYYY-AA-GG_ad-soyad_foy-11.csv`. Program yalnızca etkin sayfanın kaydedileceğini söyler; bu beklenen bir durumdur.
- CSV dosyasını Not Defteri gibi bir metin düzenleyicide aç. Hangi ayracın kullanıldığına ve Türkçe karakterlerin doğru görünüp görünmediğine bak; gözlemini günlüğe bir cümleyle yaz.
- XLSX dosyanı kapatmadan önce bir kez daha XLSX olarak kaydet (CSV'ye kaydettikten sonra açık dosya CSV olarak kalabilir).

## Teslim

İki dosya: `YYYY-AA-GG_ad-soyad_foy-11.xlsx` (`Ham`, `Temiz` ve `Gunluk` sayfalarıyla) ve aynı adlı `.csv`.

Bir YZ asistanından yardım aldıysan sorun değil; `Gunluk` sayfasının sonuna Hafta 6'daki şablonla kısa bir beyan ekle. Dosyayı bir YZ aracına yükleyeceksen bunun kurgusal bir veri olduğunu unutma; gerçek bir kurumun ya da kişinin verisini izin verilmeyen bir araca yüklemezsin.

## Kontrol listesi

- [ ] `Ham` sayfası değişmedi; bütün çalışma `Temiz` sayfasında
- [ ] Sütun adları 1. satırda; birleştirilmiş hücre, ara toplam ve not satırı yok
- [ ] Laboratuvar ve cihaz türü ayrı sütunlarda; durum bilgisi yazıyla, renk yok
- [ ] Cihaz türü, öncelik, durum ve cihaz kodu yalnızca izin verilen yazımlarda
- [ ] Bütün tarihler gerçek tarih ve `GG.AA.YYYY` biçiminde; K-033 düzeltildi
- [ ] Çözüm süreleri sayı; birim başlıkta; boş hücrelere 0 yazılmadı
- [ ] Yinelenen kayıtlar silindi; tabloda 120 kayıt var; süre toplamı 2552,2
- [ ] Tablo nesnesi, dondurulmuş üst satır, tarihe göre sıralama
- [ ] Öncelik ve Durum'da açılır liste; süre için koşullu biçimlendirme
- [ ] `Gunluk` sayfasında sorunlar, yapılan işlemler ve sayılar var
- [ ] CSV UTF-8 olarak dışa aktarıldı
