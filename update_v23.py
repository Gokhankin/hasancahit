import os

infile = 'gelecegi-yakala-v22.html'
outfile = 'gelecegi-yakala-v23.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the styling for non-media pages: remove margin-top: auto; which pushes text to the bottom.
bad_style = 'text-align: justify !important; text-indent: 2rem; line-height: 1.8; margin-top: auto; padding: 20px 10px; font-size: 1.25rem !important;'
good_style = 'text-align: justify !important; text-indent: 2rem; line-height: 1.8; padding: 20px 10px; font-size: 1.25rem !important;'

text = text.replace(bad_style, good_style)

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Kaydedildi: {outfile}")
