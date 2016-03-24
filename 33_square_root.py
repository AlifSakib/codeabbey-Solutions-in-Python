inp = input()
v = []
for i in range(inp):
	r = 1
	X, n = map(int, raw_input().split())
	if n == 0:
		v.append(r)
	else:
		while n > 0:
			r = (r + float(X/r))/2
			n -= 1
		v.append(r)
print ' '.join(str(x) for x in v)
