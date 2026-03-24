import os
import base64

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"
imagepath = r"C:\Users\Gökhan\.gemini\antigravity\brain\c7b6399c-24a8-48cc-a1d3-756fe0f73f24\media__1774367738293.jpg"

with open(imagepath, "rb") as img_f:
    img_data = img_f.read()
    b64_str = base64.b64encode(img_data).decode("utf-8")

img_entry = f'  "nadire konuk": "data:image/jpeg;base64,{b64_str}",\n'

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Add to photosData
target_photos = "const photosData = {\n"
if target_photos in content:
    content = content.replace(target_photos, target_photos + img_entry)

# Add to contributors
text = "Hasan Cahit'im,<br><br>Hayatıma güneş gibi doğdun ve benim evladım olmanın büyük mutluluğunu ve gururunu yaşıyorum. Sağlıkla başarılara koşacağın bir yaşamın olacağına inancım tam.<br><br>Bu doğum gününde de seni tüm kalbimle kucaklıyor ve tebrik ediyorum.<br><br>Nadire Konuk (Annen)"
contrib_entry = f'  {{ name: "Nadire Konuk", text: "{text}", date: "" }},\n'

target_contribs = "const contributors = [\n"
if target_contribs in content:
    content = content.replace(target_contribs, target_contribs + contrib_entry)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Added Nadire Konuk entry and photo successfully.")
