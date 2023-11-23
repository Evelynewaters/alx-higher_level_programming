#!/usr/bin/python3
"""
0x07. Python - Test-driven development
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines """
    """
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""
    for char in text:
        current_line += char
        if char in ".?:":
            formatted_line = current_line.strip()

            print(formatted_line)
            print("")

            current_line = ""

    if current_line:
        formatted_line = current_line.strip()
        print(formatted_line, end="")
