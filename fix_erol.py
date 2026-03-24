import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

target = "Doğum günün kutlu olsun. Sağlıklı, mutlu ve başarılarla dolu yılların olsun amcam.<br><br>Erol Taşkoparan\", date"
replacement = "Doğum günün kutlu olsun. Sağlıklı, mutlu ve başarılarla dolu yılların olsun amcam.\", date"

if target in content:
    content = content.replace(target, replacement)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed the duplicate Erol Taşkoparan signature.")
else:
    print("Could not find the target string to replace.")
