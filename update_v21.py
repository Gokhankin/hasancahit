import os
import re

infile = 'gelecegi-yakala-v20.html'
outfile = 'gelecegi-yakala-v21.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# JS kodu bul ve yeniden tanimla
old_txtStyle = "let txtStyle = isOzdilek ? 'text-align: center !important; max-width: 320px; margin: 0 auto; display: block;' : '';"
old_blocksHTML = '''let blocksHTML = `<div class="mem-block"><div class="mem-photo" style="${vidStyle}"><div class="mem-photo-inner">${photo1HTML}</div></div><p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:${isOzdilek ? 'center' : 'flex-end'}; ${isOzdilek ? 'max-width:320px; margin:0 auto;' : ''}"><span class="mem-author" style="${authorStyle}">${contrib.name}</span></div></div>`;'''

new_injection = '''
    let hasMedia = foundVideo || foundImg;
    // Media yoksa: text justify, line-height ferah ve ilk satir girintili pararaf
    let baseTxtStyle = hasMedia 
        ? 'text-align: center !important;' 
        : 'text-align: justify !important; text-indent: 2rem; line-height: 1.8; font-size: 1.15rem !important;';
        
    let txtStyle = isOzdilek 
        ? 'text-align: center !important; max-width: 320px; margin: 0 auto; display: block;' 
        : baseTxtStyle;

    let authorStyle = isOzdilek ? 'text-align: center !important; width: 100%; display: block;' : '';

    // Medyasi olmayanlarin Placeholder div kismini tamamen yok edelim, estetik gorunsun.
    let photoDivHTML = hasMedia ? `<div class="mem-photo" style="${vidStyle}"><div class="mem-photo-inner">${photo1HTML}</div></div>` : '';

    let blocksHTML = `<div class="mem-block">${photoDivHTML}<p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:${isOzdilek ? 'center' : 'flex-end'}; ${isOzdilek ? 'max-width:320px; margin:0 auto;' : ''}"><span class="mem-author" style="${authorStyle}">${contrib.name}</span></div></div>`;
'''

import re
text = re.sub(r"let txtStyle = .*?;\s*let authorStyle = .*?;\s*let blocksHTML = .*?`;", new_injection, text, flags=re.DOTALL)


with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Kaydedildi: {outfile}")
