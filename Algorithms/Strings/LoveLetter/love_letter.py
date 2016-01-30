def testPalindrome():
	size = len(test)
	transitions = 0
	mid = size / 2
	for i in range(mid):
		diff = abs(ord(test[i]) - ord(test[size - 1 - i]))
		transitions = transitions + diff
	print transitions

n = int(raw_input().strip())
for _ in range(n):
	test = list(raw_input().strip())
	testPalindrome()
