import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_content_lines = [
    "      <div class=\"title-page-text\">\n",
    "        Üniversite hayatının son senesinde, bu güzel heyecan ve telaşı yaşarken, bu albümle sana güzel bir anı bırakmak istedim.<br><br>\n",
    "        Bugüne kadar sana büyüklük, dostluk, arkadaşlık ve yoldaşlık yapmış güzel insanların senin için yazdıkları duygularını bu sayfalarda bulacaksın. Her birini okurken seni anılarına götüreceğine ve yüreğinde eşsiz bir iz bırakacağına inanıyorum.<br><br>\n",
    "        <em>Hayat yolunda sağlık, mutluluk, başarı ve şans sana hep eşlik etsin. Canım Yavrum...</em>\n",
    "      </div>\n",
    "      <div class=\"title-page-author\">\n",
    "        <span>Annen</span>\n",
    "        <div class=\"title-page-author-name\">Nadire Konuk</div>\n",
    "      </div>\n",
    "      <div class=\"title-page-footer\">8.2.2023</div>\n"
]

lines = lines[:333] + new_content_lines + lines[345:]

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Replacement successful")
