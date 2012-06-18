#!/usr/bin/env python2.7
import sys, re

files = sys.argv[1:]
color = True

print """
<html>
<style type="text/css">
<!--
div.yellow { background: #ffe; font-family: monospace; }
div.red { background: #fed; font-family: monospace; }
div.green { background: #efe; font-family: monospace; }
pre {padding: 0; margin: 0;}
-->
</style>
<body>
"""
for file_name in files:
  with open(file_name, 'r') as f:
    lines = f.readlines()
    headers_end = False
    headers_cnt = 0
    print "<div>"
    for line in lines:
      #print "'%s'" % (line)
      #print '#', headers_end, headers_cnt
      if line == "\r\n" and headers_cnt == 5 and not headers_end:
        headers_end = True
        if color:
          print "</div><pre>"
      if not headers_end:
        if re.match('^(From:)|(To:)|(Date:)|(Subject:)|(Cc:)', line):
          if color:
            spl = line.split(':')[0]
            sz  = len(spl)
            print "<b>%s:</b>%s<br />" % (spl, line[sz+1:-2])
          else:
            print line[-2],
          headers_cnt += 1
      else:
        if color:
          if re.match('^\-\-\-\s*$', line):
            print "</pre><div class='yellow'><pre>%s</pre></div><pre>" % (line[:-2])
          elif re.match('^\-\-\s*$', line):
            print "</pre><div class='yellow'><pre>%s</pre></div><pre>" % (line[:-2])
          elif re.match('^\+', line):
            print "</pre><div class='green'><pre>%s</pre></div><pre>" % (line[:-2])
          elif re.match('^\-', line):
            print "</pre><div class='red'><pre>%s</pre></div><pre>" % (line[:-2])
          else:
            print line[:-2]
        else:
          print line[:-2],
  print "</pre>"

