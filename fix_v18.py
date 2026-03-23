import os

infile = 'gelecegi-yakala-v17.html'
outfile = 'gelecegi-yakala-v18.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fotograflari sinirlandir (Cok buyuk olup tasmalarini engellemek icin yukseklik limitlemesi ekliyoruz)
old_img = 'photo1HTML = `<img src="${foundImg}" alt="${contrib.name}" style="width:100%; height:auto; object-fit:contain; border-radius: 2px;" />`;'
new_img = 'photo1HTML = `<img src="${foundImg}" alt="${contrib.name}" style="max-width:100%; max-height:45vh; width:auto; height:auto; object-fit:contain; border-radius: 2px;" />`;'

text = text.replace(old_img, new_img)

# 2. Isimleri sadece Ozdilek haric diger sayfalarda saga hizala. (Yazi ortali, altindaki isim sag bloklu sekilde)
old_blocks = 'let blocksHTML = `<div class="mem-block"><div class="mem-photo" style="${vidStyle}"><div class="mem-photo-inner">${photo1HTML}</div></div><p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:center; ${isOzdilek ? \'max-width:320px; margin:0 auto;\' : \'\'}"><span class="mem-author" style="${authorStyle}">${contrib.name}</span></div></div>`;'

new_blocks = 'let blocksHTML = `<div class="mem-block"><div class="mem-photo" style="${vidStyle}"><div class="mem-photo-inner">${photo1HTML}</div></div><p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:${isOzdilek ? \'center\' : \'flex-end\'}; ${isOzdilek ? \'max-width:320px; margin:0 auto;\' : \'\'}"><span class="mem-author" style="${authorStyle}">${contrib.name}</span></div></div>`;'

text = text.replace(old_blocks, new_blocks)

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Tum fotograflar duzeltildi ve isimler saga alindi. Kaydedildi: {outfile}")
