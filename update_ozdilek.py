import os

in_file = 'gelecegi-yakala-v10.html'
out_file = 'gelecegi-yakala-v11.html'

with open(in_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Metin güncellemesi
old_text = "Videonun üzerine tıklayarak ya da oynat tuşuna basarak izleyebilirsiniz."
new_text = "Doğum Günün Kutlu Olsun."

# Bazen "<br><br>Videonun üzerine..." şeklinde olabilir, o yüzden sadece hedef metni seçtik.
if old_text in text:
    text = text.replace(old_text, new_text)

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Yazı düzeltildi: {out_file}")
