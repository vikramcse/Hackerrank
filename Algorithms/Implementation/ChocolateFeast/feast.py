#!/bin/python
import sys

t = int(raw_input().strip())
for _ in xrange(t):
    n, c, m = raw_input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]

    no_of_chocolates = n / c
    if (m > no_of_chocolates):
    	print no_of_chocolates
    else:
		new_chocolates = 0
		wrappers = no_of_chocolates
		while wrappers >= m:
			new_wrappers = wrappers / m
			new_chocolates = new_chocolates + new_wrappers
			wrappers = new_wrappers + wrappers % m

		no_of_chocolates = no_of_chocolates + new_chocolates
		print no_of_chocolates