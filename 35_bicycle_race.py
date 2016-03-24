inp = input()
v = []
for i in range(inp):
	a, b, c = map(int, raw_input().split())
	ETA = a / float(b + c)
	sol = ETA * b
	v.append(sol)
print ' '.join(str(x) for x in v)