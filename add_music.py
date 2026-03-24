import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Music Button in navigation
nav_target = '<span class="nav-title">Geleceği Yakala</span>'
nav_replacement = '<button class="nav-arrow" id="musicBtn" onclick="toggleMusic()" style="font-size:1rem; padding: 2px 8px; margin-right: 6px;">🎵</button>\n  <span class="nav-title">Geleceği Yakala</span>'

if nav_target in content:
    content = content.replace(nav_target, nav_replacement)

# 2. Add Audio Element and Script
script_target = "</body>"
script_replacement = """
<!-- Background Music -->
<audio id="bgMusic" src="arka_plan_muzigi.mp3" loop></audio>
<script>
let isMusicPlaying = false;
function toggleMusic() {
  const music = document.getElementById('bgMusic');
  const btn = document.getElementById('musicBtn');
  if (isMusicPlaying) {
    music.pause();
    btn.innerHTML = '🎵';  // Play icon
    btn.style.opacity = "0.6";
    isMusicPlaying = false;
  } else {
    music.play().then(() => {
      btn.innerHTML = '🔇';  // Pause/Muted icon depending on taste, let's use a dynamic one
      btn.style.opacity = "1";
      isMusicPlaying = true;
    }).catch(err => console.log("Otomatik çalma tarayıcı tarafından engellendi."));
  }
}
</script>
</body>
"""

if script_target in content:
    content = content.replace(script_target, script_replacement)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Music button and player logic added successfully.")
