"""
I recommend you save your practicum students' project links in a Google or Excel sheet.
Then copy-paste these into markdown generator: https://www.tablesgenerator.com/markdown_tables
Then add these to the Readme.md file, and run this file from within it's folder to 
shorten github, youtube, and other links.
"""


import re

with open('../README.md', 'r') as f:
    readme = f.read()

# find github links
patterns = [r'https://github.com\S*',
            r'https://www.youtube.com\S*',
            r'https://youtu.be\S*',
            r'https*://(?!youtu)(?!github)(?!www.youtube.com)\S*']
labels = ['GitHub', 'Presentation', 'Presentation', 'Other']
for l, p in zip(labels, patterns):
    print(l, p)
    results = re.findall(p, readme)
    for r in results:
        print(r)
        readme = re.sub(re.escape(r), f'[{l}]({r})', readme)

with open('../README.md', 'w') as f:
    f.write(readme)