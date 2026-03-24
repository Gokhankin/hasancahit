import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

target = '      <div class="title-page-author">\n        <span>Annen</span>\n        <div class="title-page-author-name">Nadire Konuk</div>\n      </div>'
replacement = '      <div class="title-page-author" style="margin-top: 20px;">\n        <span>Annen</span>\n        <div class="title-page-author-name">Nadire Konuk</div>\n      </div>'

if target in content:
    content = content.replace(target, replacement)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated margin for Nadire Konuk.")
else:
    print("Could not find the target string to replace.")
