import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Aysel Konuk text
content = content.replace(
    "Nerede olursam olayım seni kalbimde taşıyacağım.<br><br>Aysel Konuk (Anneannen)",
    "Nerede olursam olayım seni kalbimde taşıyacağım."
)

# 2. Fix Nadire Konuk text
content = content.replace(
    "Bu doğum gününde de seni tüm kalbimle kucaklıyor ve tebrik ediyorum.<br><br>Nadire Konuk (Annen)",
    "Bu doğum gününde de seni tüm kalbimle kucaklıyor ve tebrik ediyorum."
)

# 3. Fix Emine Aslı Konuk text
content = content.replace(
    "Ömrümce seni çok sevecek ve değer vereceğim.<br><br>Emine Aslı Konuk (Teyzen)",
    "Ömrümce seni çok sevecek ve değer vereceğim."
)

# 4. Modify JavaScript
js_target = 'let blocksHTML = `<div class="mem-block">${photoDivHTML}<p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:${isOzdilek ? \'center\' : \'flex-end\'}; ${isOzdilek ? \'max-width:320px; margin:0 auto;\' : \'\'}"><span class="mem-author" style="${authorStyle}">${contrib.name}</span></div></div>`;'

js_replacement = """    let authorDisplayName = contrib.name;
    if (contrib.name === "Aysel Konuk") authorDisplayName = "Aysel Konuk (Anneannen)";
    if (contrib.name === "Nadire Konuk") authorDisplayName = "Nadire Konuk (Annen)";
    if (contrib.name === "Emine Aslı Konuk") authorDisplayName = "Emine Aslı Konuk (Teyzen)";
    
    let blocksHTML = `<div class="mem-block">${photoDivHTML}<p class="mem-text" style="${txtStyle}">${contrib.text}</p><div class="mem-meta" style="width:100%; justify-content:${isOzdilek ? 'center' : 'flex-end'}; ${isOzdilek ? 'max-width:320px; margin:0 auto;' : ''}"><span class="mem-author" style="${authorStyle}">${authorDisplayName}</span></div></div>`;"""

if js_target in content:
    content = content.replace(js_target, js_replacement)
    print("JS Target Replaced.")
else:
    print("JS Target Not Found!")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Made author titles dynamic while omitting them from text strings.")
