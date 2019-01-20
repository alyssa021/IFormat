from __future__ import print_function
from html.parser import HTMLParser

src_file = open("testfile.html", "r");
src_file_content = src_file.read();

parser = HTMLParser();
print(parser.feed(src_file_content));
