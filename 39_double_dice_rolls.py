inp = input()
v = []
for i in range(inp):
	a = map(int, raw_input().split())
	a1 = (a[0] % 6) + 1
	a2 = (a[1] % 6) + 1
	v.append(a1 + a2)
print ' '.join(str(x) for x in v)