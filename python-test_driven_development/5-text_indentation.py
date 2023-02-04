#!/usr/bin/python3
"""
doc
"""

def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    new_text = ""
    for char in text:
        if char in ['?', '.', ':']:
            new_text += char + "\n\n"
        else:
            new_text += char
    for line in new_text.split("\n"):
        print(line.strip())
