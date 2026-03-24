import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# I want to make the subtitle box have a fixed height so it doesn't push the video around.
# Previous: min-height:2.8rem;
# New: height: 4.5rem; display: flex; align-items: center; justify-content: center;

old_sub_style = 'min-height:2.8rem; padding:10px 16px; font-family:\'EB Garamond\',serif; font-size:1.05rem; font-style:italic; color:#1a1510; text-align:center; background:rgba(201,169,110,0.07); border-radius:0 0 6px 6px; width:100%; box-sizing:border-box; border-top:1px solid rgba(201,169,110,0.2);'
new_sub_style = 'height:72px; padding:8px 16px; font-family:\'EB Garamond\',serif; font-size:1.05rem; font-style:italic; color:#1a1510; text-align:center; background:rgba(201,169,110,0.07); border-radius:0 0 6px 6px; width:100%; box-sizing:border-box; border-top:1px solid rgba(201,169,110,0.2); display:flex; align-items:center; justify-content:center; overflow:hidden;'

if old_sub_style in content:
    content = content.replace(old_sub_style, new_sub_style)
    print("Updated subtitle style to a fixed height (72px) to prevent layout shifts.")
else:
    # Fallback search if the style was slightly different
    print("Original style string not found exactly. Trying a partial match...")
    import re
    pattern = r'min-height:2\.8rem; padding:10px 16px;'
    if re.search(pattern, content):
        content = re.sub(pattern, 'height:72px; padding:8px 16px; display:flex; align-items:center; justify-content:center;', content)
        print("Updated subtitle style using partial match.")
    else:
        print("Could not find subtitle style to update.")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")
