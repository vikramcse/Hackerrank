#!/bin/python
import sys

def separate_digits(n):
	digits = []
	while n != 0:
		rem = n % 10
		n = n / 10
		digits.append(rem)
	return digits

def process(n):
	digits = separate_digits(n)
	count = 0
	for d in digits:
		if d != 0 and n % d == 0:
			count = count + 1
	print count

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    process(n)
