# Geleceği Yakala - Dijital Anı Kitabı Proje Dokümantasyonu

Bu belge, Hasan Cahit için hazırlanan "Geleceği Yakala - Dijital Anı Kitabı" projesinin teknik altyapısını, dosya mimarisini, otomasyon betiklerini ve arayüz/tasarım kararlarını gelecekteki oturumlarda (conversations) hızlıca hatırlayabilmek adına kaydedilmiştir.

## 1. Proje Mimarisinin Temeli
Proje bağımsız ve taşınabilir tek bir HTML dosyası (`gelecegi-yakala-son.html`, `v24` vb.) olarak tasarlanmıştır. Dışarıdan hiçbir veritabanı veya asset çağırmaz. Tüm resim ve videolar Base64 formatına çevrilerek doğrudan HTML/JS içine gömülmektedir.
- JavaScript içerisindeki `contributors` dizisi (array) sayfa yapısını dinamik olarak çizer ve "İçindekiler" bölümünü otomatik indeksler.

## 2. Medya İşleme ve Üretim Boru Hattı (Pipeline)
Süreci otomatize etmek için Python betikleri kullanılır. Çalışma sırası temelde şöyledir:
1. `fotos` klasöründeki tüm resimler `.jpg`, `.png`, `.jpeg` ve ana dizindeki `.mp4` videolar `finalize_perfect.py` vb. betiklerle Base64 tipinde ayrıştırılıp JS koduna gömülür.
2. Sayfada görünecek tüm medyalar kişi isimlerine göre JS tarafında `String.includes()` ya da `toLowerCase('tr-TR')` karşılaştırmasıyla otomatik eşlenir.

## 3. Kritik Tasarım ve Stil (CSS) Kararları

Zamanla iterasyonlardan geçerek oturan kesin UI/UX kuralları bunlardır ve yeni sayfa eklenirken bozulmamasına özen gösterilmelidir:

* **Navigasyon Tuşları (Mobil Uyum):**
  - İleri-geri okları ve menü tuşları akıllı telefonda basılabilmesi için özellikle büyütüldü:
    `.nav-btn { font-size: 0.8rem !important; padding: 10px 16px !important; }`
    `.nav-arrow { font-size: 1.25rem !important; padding: 8px 18px !important; }`

* **Medyalı Sayfalar (Fotoğraf/Video İçeren):**
  - Orijinal görüntü en-boy (aspect ratio) oranlarından kaynaklı oluşan ekrandan taşma ve ekranı dikey işgal edip yazıyı itme hatalarını çözmek için fotoğraflar kısıtlanmıştır:
    `<img style="max-height: 45vh; max-width: 100%; width: auto; height: auto; object-fit: contain;">`
    
* **Medyasız Sayfalar (Sadece Yazı Olanlar):**
  - "Medya Yok" SVG yer tutucu (`fallbackPhotoHTML`) tamamen yok edilerek sayfadan kaldırılır.
  - Sadece metinden ibaret olan anılarda, **kitabi bir tasarım (Book-like typography)** kullanılır: 
    İlk satır girintili (`text-indent: 2rem`), iki yana yaslı (`text-align: justify`), ferah satır aralığı (`line-height: 1.8`) ve gövdeye tam dikey olarak ortalı (`align-items: center` ana div flexi sayesinde).

* **İsim Blokları (Author Names):**
  - Bütün sayfalarda ana yazılar konteynerına yayılırken (veyahut ortalanırken), yazar ismi (`.mem-author`) sayfanın genel sağına değil, **tam olarak bir üstündeki yazının sağ bitiş sınırına bloğa hizalı** duracak şekilde tasarlanmıştır. Bu etki `.mem-meta { justify-content: flex-end }` kullanılarak elde edilir.

* **Mehmet Özdilek Özel Kuralı:**
  - Mehmet Özdilek'in eklendiği sayfada, videonun genişliği `75% / max-width: 320px` olarak özel ayarlanmıştır.
  - Ayrıca metni (`Doğum Günün Kutlu Olsun.`) ve isminin sağa değil, **istisnai olarak tam videonun altında ortalanmış** (Center) olması istenmiştir. Dolayısıyla o kişiye özel inline `text-align: center` ve `justify-content: center; max-width: 320px; margin: 0 auto;` uygulanır.
  - **Canlı Altyazı Sistemi:** Özdilek videosu için `timeupdate` event listener'ı kullanılarak saniye bazlı bir canlı altyazı (subtitle) sistemi eklenmiştir. Altyazılar videonun hemen altındaki bir div içerisinde dinamik olarak render edilir.


## 4. İleriye Yönelik Tehlike ve Uyarılar (Hatalar)
- **JSON içi Backslash (\) Problemi:** JS içindeki `text: "..."` literal stringlerinde eğer çift slash konursa (örn. `\\"İyi ki\\"`), stringin içinde tek bir ters eğik çizgi ekrana basılır. Bu işaretleri (`\`) kaldırmak için tüm dosyadaki `\\"` karakterlerini safça  `"` ile **değiştirmeyin!** Eğer öyle yapılırsa JS'in içerisindeki string erken kapanıp "SyntaxError: Unexpected identifier" fırlatır ve sitenin tuşlarını kilitler. Değiştirme işlemi `\\\"` → `\"` olarak yapılarak **\"** şeklindeki sağlam JS kaçış (escape) dizisi korunmalıdır.

*Bu belge, projeye gelecekte de herhangi bir aşamadan, baştan veya sondan devam edilebilmesi için anıtkabir niteliğinde kalıcı belleğe (Artifacts) atılmıştır.*
