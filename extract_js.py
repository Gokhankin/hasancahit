import re

with open('gelecegi-yakala-v5.html', 'r', encoding='utf-8') as f:
    text = f.read()

script_match = re.search(r'<script>(.*?)</script>', text, re.DOTALL)
if script_match:
    script_txt = script_match.group(1)
    
    # Eliminate long base64 strings so it's readable
    script_txt = re.sub(r'\"data:image/[^\"]*base64,[^\"]+\"', '\"[BASE64_IMAGE]\"', script_txt)
    script_txt = re.sub(r'\'data:image/[^\']*base64,[^\']+\'', '\'[BASE64_IMAGE]\'', script_txt)
    
    # Print it to a temp file that is easy to view
    with open('js_logic.txt', 'w', encoding='utf-8') as f2:
        f2.write(script_txt)
    print("Extracted script logic successfully.")
else:
    print("Could not find <script> tag.")
