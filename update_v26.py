import os

infile = 'gelecegi-yakala-v24.html'
outfile = 'gelecegi-yakala-v26.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

css_append = """
<style>
/* V26 FIX - Kusursuz Mobil Scroll ve Ortalama */

/* 1. Siyah sayfalarin (arka plan) gorunmesini tamamen engellemek icin her sayfa en az ekran kadar uzun olmali */
.page, .mem-page, .title-page, .index-page {
    min-height: calc(100vh - 52px) !important;
    height: auto !important;
}

/* 2. Scroll isleminde Browser'in dogal yetenegini kullanalim, boylece 'Pull-to-refresh' (Yenileme) hatasi olusturmaz. Overflow'u serbest birakiyoruz! */
.page {
    overflow-y: visible !important;
}

.mem-page {
    overflow: visible !important;
}

/* 3. Ustten kesilen resimler (Top-Overflow) problemini cozmek icin center ozelligini siliyoruz. Margin:auto0 hilesi yapiyoruz! */
.mem-body {
    justify-content: flex-start !important; /* Tehlikeli center iptal */
    overflow: visible !important; /* Iceride div ici scroll'a GEREK YOK, normal webe birak */
}

.mem-block {
    justify-content: flex-start !important;
    flex: none !important;
    margin: auto 0 !important; /* Hucresel bosluklara gore merkezler, eger ekrandan tasiyorsa en ustten baslar! */
    padding-top: 10px !important;
    padding-bottom: 30px !important;
}

/* 4. Navigasyon barinin kaybolmamasi icin z-index guncellemesi */
.nav {
    z-index: 9999 !important;
}
</style>
"""

if '</head>' in text:
    text = text.replace('</head>', css_append + '\n</head>')

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Css Mobil Scroll/Overflow Tasmasi NATIVE Giderildi: {outfile}")
