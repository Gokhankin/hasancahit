import os

fname = 'gelecegi-yakala-v15.html'
outname = 'gelecegi-yakala-v16.html'

with open(fname, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Genelde yazıları ortala (text-align: left -> text-align: center)
# update_video_style ve finalize_perfect'ten kalan left hizalayiciyi asalim
old_text_css = 'text-align: left !important;'
new_text_css = 'text-align: center !important;'
html = html.replace(old_text_css, new_text_css)

# Bazen ayni class altinda yine solda kalmis olabilir. Garantileyelim
css_append = """
<style>
/* Yazilari merkeze, isimleri ise sag alt kosede birakan genel fix */
.mem-text {
    text-align: center !important;
}
</style>
"""
if '</head>' in html:
    html = html.replace('</head>', css_append + '\n</head>')

# 2. Mehmet Özdilek'in Videosunu Biraz Küçültelim
old_vidStyle = "let vidStyle = foundVideo ? 'width:100% !important; max-width:600px;' : '';"
new_vidStyle = "let vidStyle = foundVideo ? 'width:75% !important; max-width:320px; display:block; margin:0 auto;' : '';"
html = html.replace(old_vidStyle, new_vidStyle)

# 3. Mehmet Özdilek Altındaki Yazıyı Ve İsmi Tam Videonun Altında Ortalı ve Dar Tutalım (dışarı taşmaması için)
old_txtStyle = "let txtStyle = isOzdilek ? 'text-align: center !important;' : '';"
new_txtStyle = "let txtStyle = isOzdilek ? 'text-align: center !important; max-width: 320px; margin: 0 auto; display: block;' : '';"
html = html.replace(old_txtStyle, new_txtStyle)

old_metaDiv = '<div class="mem-meta" style="width:100%; justify-content:center;">'
new_metaDiv = '<div class="mem-meta" style="width:100%; justify-content:center; ${isOzdilek ? \'max-width:320px; margin:0 auto;\' : \'\'}">'
html = html.replace(old_metaDiv, new_metaDiv)

with open(outname, 'w', encoding='utf-8') as f:
    f.write(html)

print("Tamamlandı: " + outname)
