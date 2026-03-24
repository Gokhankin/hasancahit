import os
import base64

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"
mp3path = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\hc.mp3"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Read the new mp3 file
print(f"Reading new mp3 file from {mp3path}...")
with open(mp3path, "rb") as mp3_f:
    mp3_b64 = base64.b64encode(mp3_f.read()).decode("utf-8")

# Find the old base64 audio tag and replace it
# The old tag looks like: <audio id="bgMusic" src="data:audio/mpeg;base64,..." loop preload="auto"></audio>
import re
pattern = r'<audio id="bgMusic" src="data:audio/mpeg;base64,[^"]+" loop preload="auto"></audio>'
replacement = f'<audio id="bgMusic" src="data:audio/mpeg;base64,{mp3_b64}" loop preload="auto"></audio>'

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    print("Successfully replaced embedded mp3 with the new version.")
else:
    print("Audio tag pattern not found. Trying a simpler approach...")
    pattern_fallback = r'id="bgMusic" src="data:audio/mpeg;base64,[^"]+"'
    replacement_fallback = f'id="bgMusic" src="data:audio/mpeg;base64,{mp3_b64}"'
    if re.search(pattern_fallback, content):
        content = re.sub(pattern_fallback, replacement_fallback, content)
        print("Successfully replaced embedded mp3 using fallback pattern.")
    else:
        print("Could not find the audio tag to update.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("MP3 update script finished.")
