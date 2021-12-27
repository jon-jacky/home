"""
diary2md.py - Create markdown file (stdout) from diary format text file (stdin).

Each entry begins with a date at the beginning of a line, in dd MMM yyyy
format.   Some entries have cross references of the form 'at dd MMM yyyy'.
Most entries include URLs.   

The generated markdown file is almost the same as the input text file,
except:

1. On each date entry line, we add an HTML anchor tag.

2. We transform each '... at date ...' cross reference to a markdown link 
   to the corresponding anchor tag (the entry for that date).

3. We put <...> around each URL so it acts as a link.

The code can handle at most only one of these features on each
line in the text file.   If multiple features appear on the same line,
break the line so that no more than one feature appears on each line.
The line will appear to be joined again when the markdown is rendered.

This program generated this markdown page at github:

 https://github.com/jon-jacky/home/blob/gh-pages/design.md

from this hand-made text file:

 https://github.com/jon-jacky/home/blob/gh-pages/design.txt

This program is based on brackets.py, which only handled URLs,
not date entries or cross-references.

"""

import sys, re

url_regex = re.compile('^(.*)(https?://[\w./%~?=@+\-#&:]+)(.*)$')

date_re_string = '(\d?\d [A-Z][a-z][a-z] \d\d\d\d)'

date_regex = re.compile('^\s*' + date_re_string + '(.*)$')

xref_regex = re.compile('^(.*)' + 'at ' + date_re_string + '(.*)$')

def main():
    for line in sys.stdin:
        m = url_regex.match(line)
        if m:
            #print(line.rstrip())
            #print(m.group(2))
            print(m.group(1)+'<'+m.group(2)+'>'+m.group(3))
        else:
            m = date_regex.match(line)
            if m:
                print(line.rstrip() +
                      '  <a name="' + m.group(1).replace(' ','-') + '"></a>')
            else:
                m = xref_regex.match(line)
                if m:
                    print(m.group(1) + 'at ' + 
                          '[' + m.group(2) + ']' +
                          '(#' + m.group(2).replace(' ','-') + ')' +
                          m.group(3))
                else:
                    print(line.rstrip())

if __name__ == '__main__':
   main()

