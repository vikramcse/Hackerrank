str = raw_input().strip().lower()
alpha_positions = [0] * 26
flag = True

for c in str:
	if c != " ":
		pos = ord(c) % 26
		alpha_positions[pos] = 1

for i in alpha_positions:
	if not i:
		flag = False

if flag:
	print "pangram"
else:
	print "not pangram"
