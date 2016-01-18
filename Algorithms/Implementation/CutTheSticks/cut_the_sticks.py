#!/bin/python
import sys

def find_cut(arr):
	return min(arr)

def cut(arr):
	count = 0
	cut = find_cut(arr)
	partial = []
	for d in arr:
		c = d - cut
		if c == 0 or c:
			count = count + 1
			if c != 0:
				partial.append(c)
	print count
	return partial

def process(arr):
	while len(arr) != 0:
		arr = cut(arr)


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
process(arr)