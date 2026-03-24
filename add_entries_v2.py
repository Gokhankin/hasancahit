import os
import base64

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

# Photo for Aysel Konuk
aysel_photo_path = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\fotos\Aysel Konuk.jpeg"
with open(aysel_photo_path, "rb") as img_f:
    aysel_b64 = base64.b64encode(img_f.read()).decode("utf-8")
img_entry = f'  "aysel konuk": "data:image/jpeg;base64,{aysel_b64}",\n'

contributors_entries = [
    """  { name: "Aysel Konuk", text: "Kıymetli, değerli Hasan Cahit'im,<br><br>Varlığınla bana öyle çok şey ifade ediyorsun ki, Allah'ıma bizim olduğun için şükrediyorum. Eğitim alanındaki seçeneklerin ve üstün vasıflarınla; Atilla Dedenden aldığın özellikler ve hitabet gücünle de benim yaşam koçum oldun. Seninle gurur duyuyorum. Dolu dolu yaşadığımız güzel günlerimiz her şeye bedel.<br><br>Nerede olursam olayım seni kalbimde taşıyacağım.<br><br>Aysel Konuk (Anneannen)", date: "" },\n""",
    """  { name: "Erol Taşkoparan", text: "Hasan Cahit amcam,<br><br>Yıllar ne çabuk geçmiş. 23 yıl... Doğduğun günü hatırlıyorum. Bebekliğinde ve çocukluğunda güler yüzlü ve çok sevimliydin.<br>Şimdi de aslan gibi delikanlı oldun.<br><br>Doğum günün kutlu olsun. Sağlıklı, mutlu ve başarılarla dolu yılların olsun amcam.<br><br>Erol Taşkoparan", date: "" },\n""",
    """  { name: "Emine Aslı Konuk", text: "Benim Canım, güzel yeğenim.. Hasan Cahit'im,<br><br>Çok karlı bir 8 Şubat Saklıkent sabahında doğmuştun. Ben de dağdan uçarak inmiştim adeta. Yüreğimize ve ailemize güneş gibi doğmuştun. Sen benim yüreğimin ikinci evladısın. Ömrümce seni çok sevecek ve değer vereceğim.<br><br>Emine Aslı Konuk (Teyzen)", date: "" },\n""",
    """  { name: "Hande Naipoğlu", text: "Canımın içi iyi ki doğdun iyi ki benim kuzenim oldun. Biz ablanla iki kardeştik üç olduk tam olduk H&H&H 🥰 Hayat sana ömrün boyunca hep güzellikler sunsun hep mutlu ol şanslı bir ablayım senin gibi iyi kalpli bir kardeşe sahibim seninle gurur duyuyorum. Yeni yaşın kutlu olsun. Seni hep sevecek ömrün boyunca hep yanında olacağım ablan olarak. Seni çok öpüyorum ve seni çoook seviyorum.<br><br>Ablan Hande 😘🥰❤️🥳🧿", date: "" },\n""",
    """  { name: "Gökhan Naipoğlu", text: "Yakışıklı kardeşim, doğum günün kutlu olsun 🎂👏🏻🙂 Çok güzel bir yaş diliyorum her şey gönlünce olsun 🧿<br><br>Sevgilerimle,<br>Gökhan abin", date: "" },\n""",
    """  { name: "Akant Türel", text: "İyi ki doğdun. Seninle her şey daha eğlenceli ve güzel. Hep böyle kal, enerjin hiç bitmesin. Nice mutlu yıllara.<br><br>Akant Türel", date: "" },\n"""
]

# Read the file
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add to photosData
target_photos = "const photosData = {\n"
if target_photos in content:
    content = content.replace(target_photos, target_photos + img_entry)

# Add to contributors
target_contribs = "const contributors = [\n"
if target_contribs in content:
    content = content.replace(target_contribs, target_contribs + "".join(contributors_entries))

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Added 6 new entries successfully.")
