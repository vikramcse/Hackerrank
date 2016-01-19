#!/bin/python
import sys

n = int(raw_input().strip())

def fact(n):
	val = 1
	for i in range(1, n + 1):
		val = val * i
	print val

fact(n)
	
#OR
#print reduce(lambda x, y: x * y, range(1, n + 1))