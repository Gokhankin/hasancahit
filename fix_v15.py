import os
import re

fname = 'gelecegi-yakala-v14.html'
outname = 'gelecegi-yakala-v15.html'

with open(fname, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Mehmet Özdilek Ortalama (Center)
# Find the line that defines blocksHTML
old_blocks_html = 'let blocksHTML = `<div class="mem-block"><div class="mem-photo" style="${vidStyle}"><div class="mem-photo-inner">${photo1HTML}</div></div><p class="mem-text">${contrib.text}</p><div class="mem-meta"><span class="mem-author">${contrib.name}</span></div></div>`;'

new_blocks_html = '''
    let isOzdilek = contrib.name.toLocaleLowerCase('tr-TR').includes("özdilek") || contrib.name.toLocaleLowerCase('tr-TR').includes("mehmet");
    let txtStyle = isOzdilek ? 'text-align: center !important;' : '';
    let authorStyle = isOzdilek ? 'text-align: center !important; width:100%; display:block;' : '';
    
    let blocksHTML = `<div class="mem-block"><div class="mem-photo" style="${vidStyle}"><div class="mem-photo-inner">${photo1HTML}</div></div><p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:center;"><span class="mem-author" style="${authorStyle}">${contrib.name}</span></div></div>`;
'''

html = html.replace(old_blocks_html, new_blocks_html)

# 2. Fix the vidStyle so video is large but photos are normal
old_vidStyle = "let vidStyle = foundVideo ? 'width:75%; max-width:400px;' : '';"
new_vidStyle = "let vidStyle = foundVideo ? 'width:100% !important; max-width:600px;' : '';"

html = html.replace(old_vidStyle, new_vidStyle)

# 3. Remove the bad CSS injected for .mem-photo
css_bad = """<style>
/* Resim ve video kapsayicisini 90% dan 100%'e cikararak tam ekrana yayar, boyutu maximuma ulastirir */
.mem-photo {
    width: 100% !important;
    max-width: 600px; /* Bilgisayarda asiri devasa olmamasi icin limitleyici */
}
</style>
"""
html = html.replace(css_bad, "")

# Some extra safety if line endings differ
css_bad2 = """<style>\n/* Resim ve video kapsayicisini 90% dan 100%'e cikararak tam ekrana yayar, boyutu maximuma ulastirir */\n.mem-photo {\n    width: 100% !important;\n    max-width: 600px; /* Bilgisayarda asiri devasa olmamasi icin limitleyici */\n}\n</style>"""
html = html.replace(css_bad2, "")
html = html.replace(css_bad2.replace('\n', '\r\n'), "")
html = re.sub(r'<style>[\s\S]*?Resim ve video kapsayicisini[\s\S]*?\.mem-photo\s*{[\s\S]*?}[\s\S]*?</style>', '', html)

with open(outname, 'w', encoding='utf-8') as f:
    f.write(html)

print("Tamamlandı: " + outname)
