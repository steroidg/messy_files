#!/usr/bin/env python


import cgi, cgitb
form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>Bloop</title>"
print "</head>"
print "<body>"
print "<h2>Bleepy bloorp %s</h2>" % form["file_name"].value
print "</body>"
print "</html>"

