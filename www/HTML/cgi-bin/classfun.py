#!/usr/bin/env python3
#classfun.py

import cgi
import cgitb
import os

# functions commonly used in python

# outputs a document heading tag and 
# stylesheet link, and a title tag
#  stylesheet - name of stylesheet relative to this page
#  title - title of page 
def printDocHeading(stylesheet, title):
    print("Content-Type: text/html\n\n",\
        '<!DOCTYPE>\n',\
        #'<html language ="en">', '\n',\
        '<head>\n',\
        '<meta charset="utf-8" />\n',\
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',\
        '<meta name="author" content="">\n',\
        '<link rel="shortcut icon" href="../favicon.ico" type="image/x-icon" />\n',\
        '<link rel="icon" href="../favicon.ico" type="image/x-icon"  />\n',\
        '<link rel="STYLESHEET" href="' , stylesheet , '"  type="text/css" />\n',\
        '<title>' , title , '</title>\n',\
        '</head>\n')
        

# prints a page footer in small font with copyright
def printDocFooter():
    print("<div class='content'> \n", \
        "<div class='footer'> \n", \
        "&copy; Sam Duncan &nbsp;&nbsp;&nbsp;&nbsp;\n ", \
        "Page Last Updated:\n ", \
        " <script type='text/javascript'>\n ", \
        " document.write(document.lastModified); \n", \
        " </script> &nbsp;&nbsp;&nbsp; \n", \
        " <a href='http://validator.w3.org/check?uri=referer'> \n", \
        "  <strong>HTML</strong></a>\n ", \
        " &nbsp;&nbsp;&nbsp;&nbsp; \n", \
        " <a href='http://jigsaw.w3.org/css-validator/check?uri=referer'> \n", \
        "  <strong>CSS</strong></a>\n ", \
        "</div>\n ", \
        "</div>\n", \
        "</body>\n</html>\n")



