import os
import re

infile = 'gelecegi-yakala-v21.html'
outfile = 'gelecegi-yakala-v22.html'

with open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

new_injection = r'''    let hasMedia = foundVideo || foundImg;
    
    // Hem resimli hem resimsiz sayfalar ayni şık tasarimi kullanacak (text-justify, text-indent)
    let baseTxtStyle = hasMedia 
        ? 'text-align: justify !important; text-indent: 1.5rem; line-height: 1.6; padding: 12px 6px; font-size: 1.15rem !important;' 
        : 'text-align: justify !important; text-indent: 2rem; line-height: 1.8; margin-top: auto; padding: 20px 10px; font-size: 1.25rem !important;';
        
    let txtStyle = isOzdilek 
        ? 'text-align: center !important; max-width: 320px; margin: 0 auto; display: block;' 
        : baseTxtStyle;

    let authorStyle = isOzdilek ? 'text-align: center !important; width: 100%; display: block;' : '';'''

# Replace the block
regex_pattern = r" {4}let hasMedia = foundVideo \|\| foundImg;.*?let authorStyle = isOzdilek \? 'text-align: center !important; width: 100%; display: block;' : '';"
if re.search(regex_pattern, text, flags=re.DOTALL):
    text = re.sub(regex_pattern, new_injection, text, flags=re.DOTALL)
else:
    print("Regex match failed, trying alternative...")
    # fallback, split replace
    s = text.split('let hasMedia = foundVideo || foundImg;')
    if len(s) > 1:
        s2 = s[1].split('let authorStyle')[1]
        s3 = s2.split("display: block;' : '';")[1]
        text = s[0] + new_injection + s3

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Bitti: {outfile}")
