def findGems(rocks):
	count = 0
	levels = []
	for rock in rocks:
		level = [False] * 26
		for r in rock:
			hash = ord(r) % 26
			if not level[hash]:
				level[hash] = True
		levels.append(level)
	
	for i in range(26):
		flag = True
		for j in range(0, len(rocks)):
			if not levels[j][i]:
				flag = False
		if flag:
			count = count + 1

	print count


rocks = []
n = int(raw_input().strip())
for _ in range(n):
	rocks.append(raw_input().strip())

findGems(rocks)
