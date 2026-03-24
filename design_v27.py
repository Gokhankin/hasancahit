import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v27.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the old p1 İlk Sayfa design with a more elegant one
old_p1 = '''  <!-- İLK SAYFA -->
  <div class="page" id="p1">
    <div class="title-page" style="justify-content: center; display: flex; align-items: center; min-height: 100%;">
      <div class="title-page-text" style="font-size: 1.65rem !important; font-style: italic !important; text-align: center !important; margin: auto !important; max-width: 80% !important; font-family: 'Playfair Display', serif;">
        Mutlu ve Onurlu bir yaşam sürmen dileklerimle, Canım Yavrum Hasan Cahit'ime...
      </div>
    </div>
  </div>'''

new_p1 = '''  <!-- İLK SAYFA -->
  <div class="page" id="p1" style="background: var(--cream);">
    <div style="
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100%;
      min-height: calc(100vh - 52px);
      padding: 60px 60px;
      position: relative;
      overflow: hidden;
    ">
      <!-- Decorative top ornament -->
      <div style="
        width: 80px;
        height: 1px;
        background: var(--gold);
        margin-bottom: 10px;
      "></div>
      <div style="
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: var(--gold);
        letter-spacing: 0.3em;
        text-transform: uppercase;
        margin-bottom: 10px;
      ">✦</div>
      <div style="
        width: 80px;
        height: 1px;
        background: var(--gold);
        margin-bottom: 48px;
      "></div>

      <!-- Main dedication text -->
      <div style="
        font-family: 'Playfair Display', serif;
        font-size: 1.75rem;
        font-style: italic;
        font-weight: 400;
        color: var(--text-dark);
        text-align: center;
        line-height: 1.8;
        max-width: 78%;
        letter-spacing: 0.01em;
      ">
        Mutlu ve Onurlu bir yaşam sürmen dileklerimle,
      </div>

      <!-- Name highlight -->
      <div style="
        font-family: 'Playfair Display', serif;
        font-size: 2.1rem;
        font-style: italic;
        font-weight: 700;
        color: var(--gold);
        text-align: center;
        margin-top: 28px;
        letter-spacing: 0.05em;
      ">
        Canım Yavrum Hasan Cahit'ime…
      </div>

      <!-- Bottom ornament -->
      <div style="
        width: 120px;
        height: 1px;
        background: linear-gradient(to right, transparent, var(--gold), transparent);
        margin-top: 52px;
      "></div>
    </div>
  </div>'''

if old_p1 in content:
    content = content.replace(old_p1, new_p1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Elegant title page design applied to v27.")
else:
    print("Could not find the old p1 section.")
