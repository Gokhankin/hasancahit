import os

filepath = r"c:\Users\Gökhan\.gemini\antigravity\playground\triple-cassini\hasan cahit\gelecegi-yakala-v26.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Find existing keydown listener and add ESC key support
target = "  if (e.key === 'ArrowRight' || e.key === ' ') next();\n  if (e.key === 'ArrowLeft') prev();\n  if (e.key === 'PageDown') next();\n  if (e.key === 'PageUp') prev();"

replacement = "  if (e.key === 'ArrowRight' || e.key === ' ') next();\n  if (e.key === 'ArrowLeft') prev();\n  if (e.key === 'PageDown') next();\n  if (e.key === 'PageUp') prev();\n  if (e.key === 'Escape') goTo(0);"

if target in content:
    content = content.replace(target, replacement)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("ESC key activated - redirects to cover page (page 0).")
else:
    print("Could not find keydown listener.")
