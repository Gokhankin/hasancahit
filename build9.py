import os
import base64

html_path = 'gelecegi-yakala-v5.html'
out_path = 'gelecegi-yakala-v9.html'
fotos_dir = 'fotos'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Base64 encode the photos
photos_data = []
if os.path.isdir(fotos_dir):
    for f_name in os.listdir(fotos_dir):
        if f_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            name = os.path.splitext(f_name)[0].lower()
            path = os.path.join(fotos_dir, f_name)
            with open(path, 'rb') as pf:
                b64 = base64.b64encode(pf.read()).decode('utf-8')
            mime = "image/png" if f_name.lower().endswith('.png') else "image/jpeg"
            name_escaped = name.replace('"', '\\"')
            photos_data.append(f'  "{name_escaped}": "data:{mime};base64,{b64}"')

photos_js = "const photosData = {\n" + ",\n".join(photos_data) + "\n};\n"

# 2. Base64 encode the videos in current dir
videos_data = []
for f_name in os.listdir('.'):
    if f_name.lower().endswith('.mp4'):
        name = os.path.splitext(f_name)[0].lower()
        with open(f_name, 'rb') as vf:
            b64 = base64.b64encode(vf.read()).decode('utf-8')
        name_escaped = name.replace('"', '\\"')
        videos_data.append(f'  "{name_escaped}": "data:video/mp4;base64,{b64}"')

        # Inject contributor
        if name not in html.lower():
            idx = html.find('const contributors = [')
            if idx != -1:
                insert_idx = html.find('[', idx) + 1
                capitalized_name = name.title()
                new_entry = f'\n  {{ name: "{capitalized_name}", text: "<br><br>Videonun üzerine tıklayarak ya da oynat tuşuna basarak izleyebilirsiniz.", date: "" }},'
                html = html[:insert_idx] + new_entry + html[insert_idx:]

videos_js = "const videosData = {\n" + ",\n".join(videos_data) + "\n};\n"

# 3. Inject JS Dictionary
script_start = "const kapakPhoto ="
if script_start in html:
    html = html.replace(script_start, photos_js + "\n" + videos_js + "\n" + script_start)

# 4. Modify JS logic
old_svg_string = r'''let photo1HTML = `<svg class="mem-photo-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="8" width="34" height="24" rx="2.5" stroke="#4a3f30" stroke-width="1.4"/><circle cx="20" cy="20" r="6.5" stroke="#4a3f30" stroke-width="1.4"/><path d="M14 8l2-3h8l2 3" stroke="#4a3f30" stroke-width="1.4"/><circle cx="31" cy="13" r="1.5" fill="#4a3f30" opacity="0.4"/></svg><span class="mem-photo-label">Fotoğraf buraya eklenecek</span>`;'''

new_SVG = '''let fallbackPhotoHTML = `<svg class="mem-photo-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="8" width="34" height="24" rx="2.5" stroke="#4a3f30" stroke-width="1.4"/><circle cx="20" cy="20" r="6.5" stroke="#4a3f30" stroke-width="1.4"/><path d="M14 8l2-3h8l2 3" stroke="#4a3f30" stroke-width="1.4"/><circle cx="31" cy="13" r="1.5" fill="#4a3f30" opacity="0.4"/></svg><span class="mem-photo-label">Medya yok</span>`;
    let contribClean = contrib.name.toLocaleLowerCase('tr-TR').trim().replace(/i̇/g, 'i');
    
    let foundImg = null;
    for(let key in photosData) {
       let keyClean = key.toLocaleLowerCase('tr-TR').trim().replace(/i̇/g, 'i');
       if(contribClean === keyClean || contribClean.includes(keyClean) || keyClean.includes(contribClean)) { 
           foundImg = photosData[key]; 
           break; 
       }
    }
    
    let foundVideo = null;
    for(let key in videosData) {
       let keyClean = key.toLocaleLowerCase('tr-TR').trim().replace(/i̇/g, 'i');
       if(contribClean === keyClean || contribClean.includes(keyClean) || keyClean.includes(contribClean)) { 
           foundVideo = videosData[key]; 
           break; 
       }
    }
    
    let photo1HTML = fallbackPhotoHTML;
    if (foundVideo) {
        photo1HTML = `<video src="${foundVideo}" controls playsinline style="width:100%; height:100%; object-fit:cover; border-radius: 2px;"></video>`;
    } else if (foundImg) {
        photo1HTML = `<img src="${foundImg}" alt="${contrib.name}" style="width:100%; height:100%; object-fit:cover; border-radius: 2px;" />`;
    }
'''

if old_svg_string in html:
    html = html.replace(old_svg_string, new_SVG)

# 5. Add Responsive CSS
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
.mem-text, .mem-meta {
    width: 90% !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    margin-left: auto !important;
    margin-right: auto !important;
    box-sizing: border-box;
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
"""

html = html.replace('</head>', extra_css + '\\n</head>')

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Successfully generated {out_path}")
