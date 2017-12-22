"""
reverse.py - read todo.txt, write out recent.txt with same content
              but in reverse chron. order with most recent days first
"""

import re

date_regex = re.compile(r'^\s*\d+\s+[A-Z][a-z][a-z]\s+201[67]')

with open('todo.txt', mode='r') as fd:
    lines = fd.readlines()

date_indices = [ i for i, line in enumerate(lines) 
                 if date_regex.match(line) ]

if __name__ == '__main__':
    with open('recent.txt', mode='w') as fd:
        reversed_date_indices = list(reversed(date_indices))
        for i, index in enumerate(reversed_date_indices):
            if i > 0:
                for line in lines[index:reversed_date_indices[i-1]]:
                    fd.write(line)

