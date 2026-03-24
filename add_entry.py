import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

new_entry = """  { name: "Sümeyya Yıldız", text: "Canım Hasan Cahit,<br><br>Seni daha bebekliğinden beri tanıyorum. Büyümeni, adım adım kendi yolunu bulmanı izlemek benim için çok özel bir mutluluktu. Yıllar nasıl geçti anlamadım; bugün 23 yaşına gelmiş, pırıl pırıl bir genç oldun.<br><br>Hayatın boyunca kalbin hep güzel kalsın, yüzün hep gülsün. Yolun açık, şansın bol olsun. Seni tanımak ve büyümene tanıklık etmek benim için büyük bir gurur.<br><br>İyi ki doğdun.<br>Sevgiyle…", date: "" },\n"""

target = "const contributors = [\n"
if target in content:
    content = content.replace(target, target + new_entry)
    print("Added Sümeyya Yıldız entry successfully")
else:
    print("Could not find 'const contributors = ['.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
