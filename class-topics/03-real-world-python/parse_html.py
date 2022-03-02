import os

PATH = os.path.join("data", "index.html")

def extract_text_from_html(html):

    clean_text = ""

    should_read = True

    for char in html:

        if char == "<":
            should_read = False
        if should_read:
            clean_text = clean_text + char
        if char == ">":
            should_read = True

    return clean_text

with open(PATH, "r") as in_file:
    text = in_file.read()

clean_text = extract_text_from_html(text)
print(clean_text)
# print(text)