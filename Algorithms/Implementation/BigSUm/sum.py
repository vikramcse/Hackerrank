import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

sum = 0

for i in arr:
	sum = sum + i

print sum