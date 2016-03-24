inp = input()
v = []
for i in range(inp):
	a = map(int, raw_input().split())
	for j in a:
		if j < max(a) and j > min(a):
			v.append(j)
print ' '.join(str(x) for x in v)