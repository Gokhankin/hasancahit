import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

target = "Nice mutlu yıllara.<br><br>Akant Türel\", date: \"\""
replacement = "Nice mutlu yıllara.\", date: \"\""

if target in content:
    content = content.replace(target, replacement)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Removed duplicate Akant Türel signature.")
else:
    print("Could not find the target string.")
