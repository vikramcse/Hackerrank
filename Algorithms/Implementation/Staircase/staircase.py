import sys

n = int(raw_input().strip())

for j in range(n):
	for i in range(1, n + 1):
		if i < n - j:
			sys.stdout.write(' ')
		else:
			sys.stdout.write('#')
	print ''