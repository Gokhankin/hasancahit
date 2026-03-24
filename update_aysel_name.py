import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Aysel Konuk entry
target = "  { name: \"Aysel Konuk\", text: \"Kıymetli, değerli Hasan Cahit'im,<br><br>Varlığınla bana öyle çok şey ifade ediyorsun ki, Allah'ıma bizim olduğun için şükrediyorum. Eğitim alanındaki seçeneklerin ve üstün vasıflarınla; Atilla Dedenden aldığın özellikler ve hitabet gücünle de benim yaşam koçum oldun. Seninle gurur duyuyorum. Dolu dolu yaşadığımız güzel günlerimiz her şeye bedel.<br><br>Nerede olursam olayım seni kalbimde taşıyacağım.<br><br>Aysel Konuk\", date: \"\" },"
replacement = "  { name: \"Aysel Konuk (Anneannen)\", text: \"Kıymetli, değerli Hasan Cahit'im,<br><br>Varlığınla bana öyle çok şey ifade ediyorsun ki, Allah'ıma bizim olduğun için şükrediyorum. Eğitim alanındaki seçeneklerin ve üstün vasıflarınla; Atilla Dedenden aldığın özellikler ve hitabet gücünle de benim yaşam koçum oldun. Seninle gurur duyuyorum. Dolu dolu yaşadığımız güzel günlerimiz her şeye bedel.<br><br>Nerede olursam olayım seni kalbimde taşıyacağım.\", date: \"\" },"

if target in content:
    content = content.replace(target, replacement)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced Aysel Konuk name structure.")
else:
    print("Could not find the target string to replace.")
