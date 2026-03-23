import os

in_file = 'gelecegi-yakala-v9.html'
out_file = 'gelecegi-yakala-v10.html'

with open(in_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Metin düzeltmesi (bilir ki -> bil ki;)
old_text_1 = "Hayatın her aşamasında bunu oku, hatırla ve bilir ki"
new_text_1 = "Hayatın her aşamasında bunu oku, hatırla ve bil ki;"
text = text.replace(old_text_1, new_text_1)

# Gözden kaçmış olabilecek diğer benzer kullanımları düzeltmek için
if "bilir ki" in text and "bil ki;" not in text:
    text = text.replace("bilir ki", "bil ki;")

# CSS ile Önsöz sayfasındaki fontları büyütüp italik yapmak
css_append = """
<style>
/* Önsöz sayfası (Kapak sonrası ilk sayfa) metinleri büyütme ve italikleştirme */
.title-page-text {
    font-size: 1.45rem !important;
    font-style: italic !important;
    line-height: 1.8 !important;
}
.title-page-author span, .title-page-footer {
    font-size: 1.3rem !important;
    font-style: italic !important;
}
.title-page-author-name {
    font-size: 1.6rem !important;
    font-style: italic !important;
}

@media (max-width: 850px) {
    .title-page-text {
        font-size: 1.25rem !important;
    }
    .title-page-author span, .title-page-footer {
        font-size: 1.15rem !important;
    }
    .title-page-author-name {
        font-size: 1.4rem !important;
    }
}
</style>
"""

if '</head>' in text:
    text = text.replace('</head>', css_append + '\\n</head>')

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Bitti: {out_file}")
