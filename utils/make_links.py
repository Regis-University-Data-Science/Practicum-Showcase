"""
I recommend you save your practicum students' project links in a Google or Excel sheet.
Then copy-paste these into markdown generator: https://www.tablesgenerator.com/markdown_tables
Then add these to the Readme.md file, and run this file from within it's folder to 
shorten github, youtube, and other links.
"""


import re

with open('../README.md', 'r') as f:
    readme = f.read()

# find links that haven't already been converted
ignore_links = ['https://www.regis.edu/academics/majors-and-programs/graduate/data-science-ms)',
                'https://regis365.sharepoint.com/:v:/s/CCIS/DS/ETOCb2bBerVPueAq9uOJHncBZAxOXDsUE4F3r_pkA8E5rg?e=DJiZw8)']
patterns = [r'(https://github.com\S*)',
            r'(https://gitlab.com\S*)',
            r'(https://www.youtube.com\S*)',
            r'(https://youtu.be\S*)',
            r'(https*://(?!youtu)(?!github)(?!gitlab)(?!www.youtube.com)\S*)']
labels = ['GitHub', 'GitLab', 'Presentation', 'Presentation', 'Other']
patterns = [rf'(\[{l}\]\()*' + p for p, l in zip(patterns, labels)]
changes = 0
for l, p in zip(labels, patterns):
    print('searching:', l, ':', p)
    results = re.findall(p, readme)
    for r in results:
        if r[1] in ignore_links:
            continue
        elif r[0] == '':
            changes += 1
            print(f'changing {r[1]} to [{l}]({r[1]})')
            readme = re.sub(re.escape(r[1]), f'[{l}]({r[1]})', readme)
            print()

print(f'made {changes} changes')

with open('../README.md', 'w') as f:
    f.write(readme)