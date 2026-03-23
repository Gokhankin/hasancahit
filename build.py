import os
import base64

html_path = 'gelecegi-yakala-v5.html'
out_path = 'gelecegi-yakala-v6.html'
fotos_dir = 'fotos'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Base64 encode the photos into JS dictionary
print(f"Reading images from {fotos_dir}...")
photos_data = []
if os.path.isdir(fotos_dir):
    for file in os.listdir(fotos_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            name = os.path.splitext(file)[0].lower()
            path = os.path.join(fotos_dir, file)
            with open(path, 'rb') as f:
                b64 = base64.b64encode(f.read()).decode('utf-8')
            mime = "image/png" if file.lower().endswith('.png') else "image/jpeg"
            # escape quotes in name just in case
            name_escaped = name.replace('"', '\\"')
            photos_data.append(f'  "{name_escaped}": "data:{mime};base64,{b64}"')

photos_js = "const photosData = {\n" + ",\n".join(photos_data) + "\n};\n"

# 2. Inject JS Dictionary
script_start = "const kapakPhoto ="
if script_start in html:
    html = html.replace(script_start, photos_js + "\n" + script_start)
else:
    print("Could not find script_start")

# 3. Modify JS to use the dictionary
old_svg_string = r'''let photo1HTML = `<svg class="mem-photo-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="8" width="34" height="24" rx="2.5" stroke="#4a3f30" stroke-width="1.4"/><circle cx="20" cy="20" r="6.5" stroke="#4a3f30" stroke-width="1.4"/><path d="M14 8l2-3h8l2 3" stroke="#4a3f30" stroke-width="1.4"/><circle cx="31" cy="13" r="1.5" fill="#4a3f30" opacity="0.4"/></svg><span class="mem-photo-label">Fotoğraf buraya eklenecek</span>`;'''

new_SVG = '''let fallbackPhotoHTML = `<svg class="mem-photo-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="8" width="34" height="24" rx="2.5" stroke="#4a3f30" stroke-width="1.4"/><circle cx="20" cy="20" r="6.5" stroke="#4a3f30" stroke-width="1.4"/><path d="M14 8l2-3h8l2 3" stroke="#4a3f30" stroke-width="1.4"/><circle cx="31" cy="13" r="1.5" fill="#4a3f30" opacity="0.4"/></svg><span class="mem-photo-label">Fotoğraf yok</span>`;
    let contribClean = contrib.name.toLocaleLowerCase('tr-TR').trim().replace(/i̇/g, 'i');
    let foundImg = null;
    for(let key in photosData) {
       let keyClean = key.toLocaleLowerCase('tr-TR').trim().replace(/i̇/g, 'i');
       if(contribClean === keyClean || contribClean.includes(keyClean) || keyClean.includes(contribClean)) { 
           foundImg = photosData[key]; 
           break; 
       }
    }
    let photo1HTML = foundImg ? `<img src="${foundImg}" alt="${contrib.name}" />` : fallbackPhotoHTML;'''

if old_svg_string in html:
    html = html.replace(old_svg_string, new_SVG)
else:
    print("Could not find old_svg_string")

# 4. Add Responsive CSS overriding previous ones
extra_css = """
<style>
.mem-text { 
  text-align: left !important; 
  font-size: 1.15rem !important; 
  font-family: 'EB Garamond', serif !important;
  font-style: italic !important;
}
.mem-author {
  text-align: right !important;
  font-style: italic !important;
}
@media (max-width: 850px) {
  :root { 
    --page-w: 100vw; 
    --page-h: auto; 
    --margin-outer: 16px; 
    --margin-inner: 16px; 
    --margin-tb: 20px; 
  }
  .page { 
    width: 100vw; 
    min-height: 100vh; 
    max-width: 100vw; 
    box-shadow: none; 
    border-radius: 0; 
    box-sizing: border-box; 
    overflow-y: auto;
  }
  .book-wrap { 
    padding: 0; 
    margin-top: 52px; 
    min-height: calc(100vh - 52px); 
  }
  .mem-photo { width: 90%; }
  .mem-text { font-size: 1.05rem !important; line-height: 1.6; }
  .nav { padding: 8px 4px; }
  .cover-title-main { font-size: 2.2rem; }
  .title-page-main { font-size: 2rem; }
  .index-page { padding-bottom: 50px; }
}
</style>
</head>
"""

html = html.replace('</head>', extra_css)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Successfully wrote UI to {out_path}.")
