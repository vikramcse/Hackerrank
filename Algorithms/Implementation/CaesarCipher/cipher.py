#!/bin/python
import sys

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

def transform(str):
    t = []
    for i in str:
        if i.isalpha():
            if i >= 'A' and i <= 'Z':
                t.append(chr((ord(i) - ord('A') + k) % 26 + ord('A')))
            elif i >= 'a' and i <= 'z':
                t.append(chr((ord(i) - ord('a') + k) % 26 + ord('a')))
        else:
            t.append(i)

    print ''.join(c for c in t)

transform(s)
