import os

in_file = 'gelecegi-yakala-v11.html'
out_file = 'gelecegi-yakala-v12.html'

with open(in_file, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Resimlerin (ve videonun) içine gömülmüş stili (kırpmayı) düzelt
text = text.replace('width:100%; height:100%; object-fit:cover;', 'width:100%; height:auto; object-fit:contain; max-height: 60vh;')

# 2. Resmin dışındaki div karesinin özelliklerini esnek, doğal boyuta adapte olacak şekilde ez
css_append = """
<style>
/* Resimleri kare yapmaya zorlayan kırpma ayarlarını iptal eder, özgün orana bırakır */
.mem-photo {
    aspect-ratio: auto !important;
    height: auto !important;
    background: transparent !important;
    border: none !important;
    max-height: none !important;
}
</style>
"""

if '</head>' in text:
    text = text.replace('</head>', css_append + '\\n</head>')

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Resim kırpmaları kaldırıldı: {out_file}")
