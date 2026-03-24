import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

target = "Nerede olursam olayım seni kalbimde taşıyacağım.\", date"
replacement = "Nerede olursam olayım seni kalbimde taşıyacağım.<br><br>Aysel Konuk\", date"

if target in content:
    content = content.replace(target, replacement)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Restored Aysel Konuk without (Anneannen).")
else:
    print("Could not find the target string to replace.")
