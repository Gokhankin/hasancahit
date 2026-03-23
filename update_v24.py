import os

infile = 'gelecegi-yakala-v23.html'
outfile = 'gelecegi-yakala-v24.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Tuslari buyut (mobil uyumlu tiklanabilir hedefler)
css_append = """
<style>
/* Mobil icin ulasilabilir, kolay tiklanabilir buyuk tuslar */
.nav-btn {
    font-size: 0.8rem !important;
    padding: 10px 16px !important;
}
.nav-arrow {
    font-size: 1.25rem !important;
    padding: 8px 18px !important;
}
.nav-title {
    font-size: 0.95rem !important;
}
.page-counter {
    font-size: 0.75rem !important;
}
</style>
"""

if '</head>' in text:
    text = text.replace('</head>', css_append + '\n</head>')

# 2. Gökhan KIN eklentisi
new_contributor = '''
  { name: "Gökhan Kın", text: "Ailesini gururlandıran, çalışkan ve beyefendi bir genç adam olduğunu görmek bizler için en büyük mutluluk. Yeni yaşının sana tüm hedeflerine ulaşabilmen için başarı ve şans getirmesini dilerim. İyi ki doğdun Hasan Cahit.", date: "" },
'''

text = text.replace('const contributors = [', 'const contributors = [\n' + new_contributor)

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Islem basarili: {outfile}")
