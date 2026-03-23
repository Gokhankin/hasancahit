import os

html_path = 'gelecegi-yakala-v7.html'
out_path = 'gelecegi-yakala-v8.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We will inject the CSS override right before </head>
css_fix = """
<style>
/* İsim ve Üst Yazı hizalama problemi düzeltmesi */
.mem-text, .mem-meta {
    width: 90% !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    box-sizing: border-box;
}
@media (max-width: 850px) {
    .mem-text, .mem-meta {
        width: 90% !important;
    }
}
</style>
"""

if '</head>' in html:
    html = html.replace('</head>', css_fix + '\n</head>')
else:
    print("Could not find </head>")

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Alignment fix applied successfully. Saved to {out_path}.")
