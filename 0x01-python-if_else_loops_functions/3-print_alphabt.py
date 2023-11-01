#!/usr/bin/python3
# Author - Evelyne Ngene

for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
