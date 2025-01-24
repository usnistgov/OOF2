# Fix the external (non-NIST) URLs in manual.html by piping them
# through redirect.py, the NIST exit script.
#
# This script reads html from stdin, replaces
#   href="http://
# with
#   href="/cgi-bin/redirect.py?url=http
# (or the same with https) in all external links, and writes the
# result to stdout.  External links are ones that don't contain
# "nist.gov".

import sys
import re

linkregex = re.compile(r'href="http(s?)://')
nistlinkregex = re.compile(r'href="http(s?)://(.+?)\.nist\.gov(.*?)"')

for line in sys.stdin:
    newline = ""
    lastpos = 0
    # Loop over links in the line
    for m in linkregex.finditer(line):
        if not nistlinkregex.match(line[m.start():]):
            # Include everything from line up to the start of the match
            newline += line[lastpos:m.start()]
            newline += f'href="/cgi-bin/redirect.py?url=http{m[1]}://'
            lastpos = m.end()
        else:
            # Found internal NIST link
            newline += line[lastpos:m.end()]
            lastpos = m.end()
    newline += line[lastpos:]
    print(newline, end="")
