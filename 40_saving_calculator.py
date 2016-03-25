inp = input()
v = []
for i in range(inp):
	s, r, p = map(int, raw_input().split())
	# s, r, p = int(a[0]), int(a[1]), float(a[2])
	count = 0
	old_sum = s
	while old_sum < r:
		s = old_sum + s * (float(p)/100)
		old_sum = s
		count += 1
	v.append(count)
print ' '.join(str(x) for x in v)
