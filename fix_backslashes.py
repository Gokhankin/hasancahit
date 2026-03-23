import os

infile = 'gelecegi-yakala-v16.html'
outfile = 'gelecegi-yakala-v17.html'

with open(infile, 'r', encoding='utf-8') as f:
    content = f.read()

# Javascript icindeki \\" (eski bir script cift kacis yapmis) ifadesini \" yapalim.
# Boylece sayfada \" seklinde degil sadece " seklinde gorunecektir (JS parselarken 1 kacisi yutar).
content = content.replace(r'\\"', r'\"')

# Eger literal olarak ekranda veya kaynak kodda gorunen gereksiz \n metinleri varsa bunlari dogruca satir basina cevirelim
content = content.replace(r'\n</head>', '\n</head>')

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Baclslashes cleaned. Saved to {outfile}")
