import os

html_path = 'gelecegi-yakala-son.html'
out_path = 'gelecegi-yakala-son.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_vid = '<video src="${foundVideo}" controls playsinline style="width:100%; height:auto; object-fit:contain; border-radius: 2px; max-height:80vh;"></video>'
new_vid = '<video src="${foundVideo}" controls playsinline style="width:100%; aspect-ratio:4/5; object-fit:cover; border-radius: 2px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);"></video>'

if old_vid in text:
    text = text.replace(old_vid, new_vid)
else:
    print("Eski video etiketi tam eplesmedi, regex deneniyor.")
    import re
    text = re.sub(r'<video src="\$\{foundVideo\}"[^>]*></video>', new_vid, text)

# Videoyu ve gorselleri sayfada kaplanabilir miktarda en fazla büyütmek icin
css_append = """
<style>
/* Resim ve video kapsayicisini 90% dan 100%'e cikararak tam ekrana yayar, boyutu maximuma ulastirir */
.mem-photo {
    width: 100% !important;
    max-width: 600px; /* Bilgisayarda asiri devasa olmamasi icin limitleyici */
}
</style>
"""

if '</head>' in text:
    text = text.replace('</head>', css_append + '\\n</head>')

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Video büyutuldu ve kenarları kırpıldı -> {out_path}")
