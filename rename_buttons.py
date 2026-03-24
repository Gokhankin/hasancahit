import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    'onclick="goTo(1)">İlk Sayfa</button>',
    'onclick="goTo(1)">Giriş</button>'
)
content = content.replace(
    'onclick="goTo(3)">İçindekiler</button>',
    'onclick="goTo(3)">İçerik</button>'
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Nav button labels updated: İlk Sayfa → Giriş, İçindekiler → İçerik.")
