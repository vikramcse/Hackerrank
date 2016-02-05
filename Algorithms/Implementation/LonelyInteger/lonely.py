import sys

N = int(raw_input())

arr = map(int, raw_input().strip().split(" "))

length = len(arr)
if length > 1:
	ans = 0
	for i in arr:
		ans = ans ^ i
	print ans
else:
	print arr[0]