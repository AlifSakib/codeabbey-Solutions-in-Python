inp = input()
v = []
for i in range(inp):
	a = map(int, raw_input().split())
	sum = 0
	for j in range(a[2]):
		s= a[0] + a[1] * j
		sum += s
	v.append(sum)

print ' '.join(str(x) for x in v)