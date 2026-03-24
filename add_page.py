import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_html = """<div class="nav">
  <button class="nav-btn" onclick="goTo(0)">Kapak</button>
  <button class="nav-btn" onclick="goTo(1)">İlk Sayfa</button>
  <button class="nav-btn" onclick="goTo(2)">Önsöz</button>
  <button class="nav-btn" onclick="goTo(3)">İçindekiler</button>
  <div class="nav-sep"></div>
  <span class="nav-title">Geleceği Yakala</span>
  <div class="nav-sep"></div>
  <div class="nav-arrows">
    <button class="nav-arrow" onclick="prev()">←</button>
    <span class="page-counter" id="counter">1 / ?</span>
    <button class="nav-arrow" onclick="next()">→</button>
  </div>
</div>

<div class="book-wrap" id="bookWrap">

  <!-- KAPAK -->
  <div class="page active" id="p0">
    <div class="cover-overlay"></div>
    <div class="cover-title">
      <div class="cover-title-main">Geleceği Yakala</div>
      <div class="cover-title-sub">Anılar ve Dilekler</div>
      <div class="cover-year">2026</div>
    </div>
    <div class="cover-footer">
      <div class="cover-author">Hasan Cahit AKINCIOĞLU</div>
      <div class="cover-line"></div>
    </div>
  </div>

  <!-- İLK SAYFA -->
  <div class="page" id="p1">
    <div class="title-page" style="justify-content: center; display: flex; align-items: center; min-height: 100%;">
      <div class="title-page-text" style="font-size: 1.65rem !important; font-style: italic !important; text-align: center !important; margin: auto !important; max-width: 80% !important; font-family: 'Playfair Display', serif;">
        Mutlu ve Onurlu bir yaşam sürmen dileklerimle, Canım Yavrum Hasan Cahit'ime...
      </div>
    </div>
  </div>

  <!-- ÖNSÖZ -->
  <div class="page" id="p2">
    <div class="title-page">
      <div class="title-page-main">Önsöz</div>
      <div class="title-page-divider"></div>
      <div class="title-page-text">
        Üniversite hayatının son senesinde, bu güzel heyecan ve telaşı yaşarken, bu albümle sana güzel bir anı bırakmak istedim.<br><br>
        Bugüne kadar sana büyüklük, dostluk, arkadaşlık ve yoldaşlık yapmış güzel insanların senin için yazdıkları duygularını bu sayfalarda bulacaksın. Her birini okurken seni anılarına götüreceğine ve yüreğinde eşsiz bir iz bırakacağına inanıyorum.<br><br>
        <em>Hayat yolunda sağlık, mutluluk, başarı ve şans sana hep eşlik etsin. Canım Yavrum...</em>
      </div>
      <div class="title-page-author">
        <span>Annen</span>
        <div class="title-page-author-name">Nadire Konuk</div>
      </div>
      <div class="title-page-footer">8.2.2023</div>
    </div>
  </div>

  <!-- İÇİNDEKİLER -->
  <div class="page" id="p3">
    <div class="index-page">
      <div class="index-title">İçindekiler</div>
      <div class="index-content" id="indexContent"></div>
      <div class="index-page-num">
        <span class="index-footer-title">Geleceği Yakala</span>
        <span class="index-footer-num">3</span>
      </div>
    </div>
  </div>

</div>
"""

# The section to replace is from Line 299 (<div class="nav">) to Line 357 (</div> just before <script>)
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<div class="nav">' in line and start_idx == -1:
        start_idx = i
    if '<script>' in line and end_idx == -1:
        end_idx = i

if start_idx != -1 and end_idx != -1:
    lines = lines[:start_idx] + [new_html] + lines[end_idx:]

# Next, update the "3 + idx" to "4 + idx" stuff
for i, line in enumerate(lines):
    if "const pageNum = 3 + idx;" in line:
        if "// Sayfa" in line:
            lines[i] = "    const pageNum = 4 + idx; // Sayfa 4'ten başla (0=kapak, 1=ilksayfa, 2=önsöz, 3=içindekiler)\n"
        else:
            lines[i] = "    const pageNum = 4 + idx;\n"
            
    # Also CSS ID #p1 -> #p1, #p2. We had #p1 for title page, #p2 for index.
    # We should add a CSS rule for #p1, #p2, #p3
    if "#p1 { background: var(--cream); }" in line:
        lines[i] = "#p1, #p2, #p3 { background: var(--cream); }\n"
    if "#p2 { background: var(--cream); }" in line:
        lines[i] = ""

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Modified HTML and JS for 'İlk Sayfa'.")
