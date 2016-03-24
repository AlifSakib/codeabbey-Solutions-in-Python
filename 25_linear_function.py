def slope(x1, y1, x2, y2):
	return int((y2 - y1)/(x2 - x1))

def intercept(x, y, m):
	return int(y - x * m)

inp = input()
v = []
for i in range(inp):
	a = map(int, raw_input().split())
	m = slope(a[0], a[1], a[2], a[3])
	b = intercept(a[0], a[1], m)
	s = '('+str(m)+' '+str(b)+')'
	v.append(s)
print ' '.join(str(x) for x in v)