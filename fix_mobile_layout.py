import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update html, body to use dvh and overscroll-behavior
old_body_css = '''html, body {
  min-height: 100vh;
  background: #1a1714;
  display: flex; flex-direction: column; align-items: center;
  font-family: 'EB Garamond', serif;
}'''

new_body_css = '''html, body {
  height: 100%;
  min-height: 100dvh;
  background: #1a1714;
  display: flex; flex-direction: column; align-items: center;
  font-family: 'EB Garamond', serif;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  overscroll-behavior-y: none;
}'''

if old_body_css in content:
    content = content.replace(old_body_css, new_body_css)
    print("Updated body CSS for mobile scrolling.")

# 2. Update book-wrap margin and min-height
old_book_wrap = '.book-wrap { margin-top: 52px; width: 100%; min-height: calc(100vh - 52px); display: flex; align-items: center; justify-content: center; padding: 36px 16px 52px; }'
new_book_wrap = '.book-wrap { margin-top: 60px; width: 100%; min-height: calc(100dvh - 60px); display: flex; align-items: center; justify-content: center; padding: 20px 10px 40px; }'

if old_book_wrap in content:
    content = content.replace(old_book_wrap, new_book_wrap)
    print("Updated book-wrap for mobile.")

# 3. Handle @media query fixes
old_media = '''  .page { 
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
  }'''

new_media = '''  .page { 
    width: 100vw; 
    min-height: calc(100dvh - 60px); 
    height: auto;
    max-width: 100vw; 
    box-shadow: none; 
    border-radius: 0; 
    box-sizing: border-box; 
    overflow-y: visible;
    overflow-x: hidden;
  }
  .book-wrap { 
    padding: 0; 
    margin-top: 60px; 
    min-height: calc(100dvh - 60px); 
    display: block;
  }'''

if old_media in content:
    content = content.replace(old_media, new_media)
    print("Updated media queries for mobile-first scrolling.")

# 4. Ensure nav has a decent height on mobile
old_nav = '  background: rgba(14,12,10,0.96);'
new_nav = '  background: rgba(14,12,10,0.96); min-height: 60px;'
if old_nav in content:
    content = content.replace(old_nav, new_nav)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("CSS refined for mobile stability.")
