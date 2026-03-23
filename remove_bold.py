import os

html_path = 'gelecegi-yakala-son.html'
out_path = 'gelecegi-yakala-son.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

css_append = """
<style>
/* Hazırlayan ve isminin kalınlığını (bold) sıfırla, normal ağırlığa döndür */
.title-page-author span, .title-page-author-name {
    font-weight: normal !important;
    font-weight: 400 !important;
}
</style>
"""

if '</head>' in text:
    text = text.replace('</head>', css_append + '\\n</head>')

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Bold yapısı başarıyla kaldırıldı.")
