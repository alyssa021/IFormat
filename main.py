from __future__ import print_function
import re;

src_file = open("test/html/test1.html", "r");
src_file_content = src_file.read();

class HTML_Tag:
  def __init__(self, raw_tag):
    re_exp = re.match("<[/]?(.*?)>", raw_tag);
    self.name = re_exp.group(1);

    if("/" in raw_tag):
      self.closing = True;
    else:
      self.closing = False;

is_tag = False;
tags = [];
for ch in src_file_content:
  if ch == "<":
    tag = "";
    is_tag = True;

  elif ch == ">":
    tag += ch;
    is_tag = False;

    tags.append(tag);

  if is_tag:
    tag += ch;

for tag in tags:
  _tag = HTML_Tag(tag);
  print(_tag.name);
