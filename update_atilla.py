import os

infile = 'gelecegi-yakala-v19.html'
outfile = 'gelecegi-yakala-v20.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# Eski metin (Atilla Konuk)
old_line = '{ name: "Atilla Konuk", text: "Oğlum, görkemli yarınlar seni bekliyor. Tüm engelleri aşıp başarılar elde etmeni diliyorum. Seni çok seviyorum.", date: "" },'

# Yeni metin
new_line = '{ name: "Atilla Konuk", text: "Hasan-Cahit\'cim, kuzenimsin diye demiyorum, seni hep sevmişimdir, ama yeter artık daha fazla uzama, komplexe giriyorum, kuzen muzen dinlemem...", date: "" },'

if old_line in text:
    text = text.replace(old_line, new_line)
else:
    # Eger encode/decode problemi veya spacing farki varsa
    import re
    text = re.sub(r'\{\s*name:\s*"Atilla Konuk",\s*text:\s*".*?",\s*date:\s*""\s*\},', new_line, text)

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print("Atilla Konuk yazisi guncellendi.")
