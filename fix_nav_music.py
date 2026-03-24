import os
import base64

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"
mp3path = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\hc.mp3"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove nav title "Geleceği Yakala" and its surrounding separators
old_nav = '''  <div class="nav-sep"></div>
  <span class="nav-title">Geleceği Yakala</span>
  <div class="nav-sep"></div>'''
if old_nav in content:
    content = content.replace(old_nav, '')
    print("Removed 'Geleceği Yakala' nav title.")
else:
    print("Nav title not found, trying with music button...")
    old_nav2 = '''<button class="nav-arrow" id="musicBtn" onclick="toggleMusic()" style="font-size:1rem; padding: 2px 8px; margin-right: 6px;">🎵</button>\n  <span class="nav-title">Geleceği Yakala</span>'''
    if old_nav2 in content:
        content = content.replace(old_nav2, '<button class="nav-arrow" id="musicBtn" onclick="toggleMusic()" style="font-size:1rem; padding: 2px 8px; margin-right: 6px;">🎵</button>')
        print("Removed 'Geleceği Yakala' from next to music button.")

# 2. Embed the mp3 as base64 so it works on mobile (no external file needed)
print("Reading mp3 file...")
with open(mp3path, "rb") as mp3_f:
    mp3_b64 = base64.b64encode(mp3_f.read()).decode("utf-8")
    
old_audio = '<audio id="bgMusic" src="hc.mp3" loop></audio>'
new_audio = f'<audio id="bgMusic" src="data:audio/mpeg;base64,{mp3_b64}" loop preload="auto"></audio>'

if old_audio in content:
    content = content.replace(old_audio, new_audio)
    print("Embedded mp3 as base64 for mobile compatibility.")
else:
    print("Audio tag not found.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")
