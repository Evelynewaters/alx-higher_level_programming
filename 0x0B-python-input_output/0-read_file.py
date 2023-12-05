#!/usr/bin/python3
""" Read File """

def read_file(filename=""):
    """ Read File """
    with open(filename, encoding="utf-8") as file:
        for line in file.readlines():
            print(line, end='')
