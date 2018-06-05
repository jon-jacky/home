"""
brackets.py - put <...> around each URL for markdown previewer
"""

import sys, re

url_regex = re.compile('^(.*)(https?://[\w./%~?=\-]+)(.*)$')

for line in sys.stdin:
    m = url_regex.match(line)
    if m: 
        #print(line.rstrip())
        #print(m.group(2))
        print(m.group(1)+'<'+m.group(2)+'>'+m.group(3))
    else:
        print(line.rstrip())
