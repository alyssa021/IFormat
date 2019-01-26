from __future__ import print_function

src_file = open("test/html/test1.html", "r");
src_file_content = src_file.read();

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

print(tags);
