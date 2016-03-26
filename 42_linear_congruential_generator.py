inp = input()
v = []
for i in range(inp):
	a = map(int, raw_input().split())
	xo = a[3]
	while a[4] > 0:
		xnext = (a[0] * xo + a[1]) % a[2]
		xo = xnext
		a[4] = a[4] - 1
	v.append(xo)
print ' '.join(str(x) for x in v)