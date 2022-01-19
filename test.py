#!/usr/bin/env python
a = [1,2,3,4,5,6]
b = ['a','b','c','d','e','f']
for x,y in zip(a, b):
    if len(a) == len(b):
        print(x,y)
    else:
        print("You are a gimp")
        exit(255)

