import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Update the audio source to hc.mp3
target = 'src="arka_plan_muzigi.mp3"'
replacement = 'src="hc.mp3"'

if target in content:
    content = content.replace(target, replacement)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Audio source updated to hc.mp3")
else:
    print("Could not find audio source tag.")
