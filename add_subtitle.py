import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the Ozdilek video generation to add subtitle support
old_video_html = '''    if (foundVideo) {
        photo1HTML = `<video src="${foundVideo}" controls playsinline style="width:100%; aspect-ratio:4/5; object-fit:cover; border-radius: 2px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);"></video>`;'''

new_video_html = '''    if (foundVideo) {
        const isOzd = contrib.name.toLocaleLowerCase('tr-TR').includes("özdilek") || contrib.name.toLocaleLowerCase('tr-TR').includes("mehmet");
        const vidId = `vid-${idx}`;
        photo1HTML = `<div style="position:relative; width:100%; display:flex; flex-direction:column; align-items:center; gap:0;">
          <video id="${vidId}" src="${foundVideo}" controls playsinline style="width:100%; aspect-ratio:4/5; object-fit:cover; border-radius: 2px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);"></video>
          ${isOzd ? `<div id="sub-${vidId}" style="min-height:2.8rem; padding:10px 16px; font-family:'EB Garamond',serif; font-size:1.05rem; font-style:italic; color:#1a1510; text-align:center; background:rgba(201,169,110,0.07); border-radius:0 0 6px 6px; width:100%; box-sizing:border-box; border-top:1px solid rgba(201,169,110,0.2);">&nbsp;</div>` : ''}
        </div>`;'''

if old_video_html in content:
    content = content.replace(old_video_html, new_video_html)
    print("Updated video HTML for subtitle support.")
else:
    print("Could not find old video HTML.")

# 2. Add subtitle data and event listener after page is appended
old_append = '''    bookWrap.appendChild(memPage);
  });
  
  pages = document.querySelectorAll('.page');'''

new_append = '''    bookWrap.appendChild(memPage);

    // Ozdilek Subtitle System
    (function() {
      const isOzdCheck = contrib.name.toLocaleLowerCase('tr-TR').includes("ozdilek") || contrib.name.toLocaleLowerCase('tr-TR').includes("mehmet");
      if (!isOzdCheck || !foundVideo) return;
      const vidId = `vid-${idx}`;
      const subtitles = [
        { start: 0,  end: 4,  text: "Sevgili Hasan Cahit, benim yakışıklı kardeşim." },
        { start: 4,  end: 10, text: "Her şeyden önce senin gibi kalbi güzel, anne babanın çocuğu olduğu için çok şanslısın." },
        { start: 10, end: 12, text: "Zaman çabuk geçiyor." },
        { start: 12, end: 15, text: "Göz açıp kapayıncaya kadar büyüdün." },
        { start: 15, end: 17, text: "Yeni yaşını kutluyorum." },
        { start: 17, end: 22, text: "Şansın bol, bahtın açık, başarıların daim olsun." },
        { start: 22, end: 26, text: "Sevdiklerinle nice nice nice uzun ömürlü yaşlar diliyorum." },
        { start: 26, end: 29, text: "İyi ki doğdun, iyi ki varsın, seviliyorsun." },
        { start: 29, end: 30, text: "Görüşmek dileğiyle." },
        { start: 30, end: 99, text: "Sevgiler, selamlar." }
      ];
      const vid = document.getElementById(vidId);
      const sub = document.getElementById(`sub-${vidId}`);
      if (vid && sub) {
        vid.addEventListener('timeupdate', function() {
          const t = vid.currentTime;
          const found = subtitles.find(s => t >= s.start && t < s.end);
          sub.textContent = found ? found.text : '\\u00a0';
        });
        vid.addEventListener('ended', function() {
          sub.textContent = '\\u00a0';
        });
      }
    })();
  });
  
  pages = document.querySelectorAll('.page');'''

if old_append in content:
    content = content.replace(old_append, new_append)
    print("Added Ozdilek subtitle event listener.")
else:
    print("Could not find append position.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")
