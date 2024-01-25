# convert.py

import markdown

# TODO have this take the source file as an argument instead of hardcoding it
title = 'home'
source_file = 'src/{}.md'.format(title)
target_file = 'published/{}.html'.format(title)


with open(source_file, 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open(target_file, 'w') as f:
    f.write(html)
