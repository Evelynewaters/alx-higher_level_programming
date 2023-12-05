#!/usr/bin/python3

def pascal_triangle(n):
    for i in range(1, n):
        for j in range(1, n):
            print(i, end="")
        print()


pascal_triangle(5)
