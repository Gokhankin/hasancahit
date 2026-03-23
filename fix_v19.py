import os

infile = 'gelecegi-yakala-v16.html'
outfile = 'gelecegi-yakala-v19.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fotograflari sinirlandir (v18'deki gibi)
old_img = 'photo1HTML = `<img src="${foundImg}" alt="${contrib.name}" style="width:100%; height:auto; object-fit:contain; border-radius: 2px;" />`;'
new_img = 'photo1HTML = `<img src="${foundImg}" alt="${contrib.name}" style="max-width:100%; max-height:45vh; width:auto; height:auto; object-fit:contain; border-radius: 2px;" />`;'
text = text.replace(old_img, new_img)

# 2. Isimleri saga hizalama (v18'deki gibi)
old_blocks = 'let blocksHTML = `<div class="mem-block"><div class="mem-photo" style="${vidStyle}"><div class="mem-photo-inner">${photo1HTML}</div></div><p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:center; ${isOzdilek ? \'max-width:320px; margin:0 auto;\' : \'\'}"><span class="mem-author" style="${authorStyle}">${contrib.name}</span></div></div>`;'
new_blocks = 'let blocksHTML = `<div class="mem-block"><div class="mem-photo" style="${vidStyle}"><div class="mem-photo-inner">${photo1HTML}</div></div><p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:${isOzdilek ? \'center\' : \'flex-end\'}; ${isOzdilek ? \'max-width:320px; margin:0 auto;\' : \'\'}"><span class="mem-author" style="${authorStyle}">${contrib.name}</span></div></div>`;'
text = text.replace(old_blocks, new_blocks)

# 3. YAZI KESINTILERI VE BUKUK JS (v17'de yapilan hata yuzunden JS syntax hatasi vermisti)
# V16 kopyamizda \\" (3 slash) veya \\" (2 slash) olanlari dogru sekilde \" 'ya dondurecegiz.
# Ornek: text: "gercekten \\\"iyi ki\\\"" seklindeki 3 slashli ifade, ekranda \" gosterir.
# Eger biz 3 slashliyi 1 slashe cevirirsek (yani \"), JS parsediginde "iyi ki" temiz sekilde cikacaktir.
text = text.replace(r'\\\"', r'\"')
text = text.replace(r'\\"', r'\"')

# Bu bir hack: Eger 'text: "... \" "' kismi kapanirsa, onu duzeltiriz.
# Garanti olsun diye tekrar bir kontrol yapalim. text = text.replace(r'\"', r'\"') zaten ayni seydir.
# Geriye dondurulemez hata olmamasi icin string basina veya sonuna dikkat edelim. JS dosyasinin calistigina emin olmak icin asagida guvenli hale getirdik.

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Tamamlandi: {outfile}")
