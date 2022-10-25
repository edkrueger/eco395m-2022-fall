import os

PATH = os.path.join("data", "index.html")
OUT_PATH = os.path.join("data", "index.txt")

def strip_html(html):

    text = ""

    should_concat = None

    for char_ in html:

        if char_ == "<":
            should_concat = False
        
        if should_concat:
            text += char_

        if char_ == ">":
            should_concat = True
    return text

with open(PATH, "r") as f:
    html = f.read()

text = strip_html(html)

with open(OUT_PATH, "w+") as out_file:
    out_file.write(text)

