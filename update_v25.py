import os

infile = 'gelecegi-yakala-v24.html'
outfile = 'gelecegi-yakala-v25.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# Mobil tasmalarda ust tarafin kesilip sayfanin yukarisina kacmasini engelleyen, hem yatay hem dikey kaydirma / margin auto duzeltmesi.
css_append = """
<style>
/* Mobil Flex Tasmasi - Yukarida Kalan Resimleri & Siyah Bosluklari Duzeltme (V25 Fix) */

/* Scroll sadece icerigin kendi alaninda serbest olsun, ana sayfa stabil kalsin */
.mem-page {
    overflow: hidden !important; 
}

/* Flexbox'in tehlikeli "center" yasasini flex-start'a cevirip overflow ekliyoruz. Bu ustten tasmayi iptal eder, kaydirmayi mumkun kilar */
.mem-body {
    justify-content: flex-start !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    padding-bottom: 30px !important; /* Alt bossluk rahatligi */
    min-height: 0 !important;
}

/* Eger icerik kisaysa kendini zarifce ortalamasi icin Flex oynamasi (margin auto calisirsa ortalar, sigmazsa yukaridan payli baslar) */
.mem-block {
    justify-content: flex-start !important;
    flex: none !important;
    margin: auto 0 !important;
    padding-top: 10px !important;
}

/* Ayrica Mehmet Ozdilek gibi max-width 320px ile sinirlanmis kisimlarin kaydirma icinde sekil bozuklugunu tamamen ortadan kaldirmasi icin */
.mem-meta {
    flex-shrink: 0;
}
</style>
"""

if '</head>' in text:
    text = text.replace('</head>', css_append + '\n</head>')

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Css Mobil Scroll/Overflow Tasmasi Giderildi: {outfile}")
