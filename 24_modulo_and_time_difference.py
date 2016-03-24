inp = input()
v = []
for i in range(inp):
	a = map(int, raw_input().split())
	a1, b1, c1, d1 = a[0], a[1], a[2], a[3]
	a2, b2, c2, d2 = a[4], a[5], a[6], a[7]
	d = a2 - a1
	if b2 < b1:
		h = (24 - b1) + b2
		d = d - 1
	else:
		h = b2 - b1	
	if c2 < c1:
		m = (60 - c1) + c2
		h = h - 1
	else:
		m = c2 - c1	
	if d2 < d1:
		s = (60 - d1) + d2
		if m - 1 < 0:
			m = 60 - 1
			if h - 1 < 0:
				h = 24 - 1
				d = d - 1
			else:
				h = h - 1
		else:
			m = m - 1 
	else:
		s = d2 - d1	
	v.append("(%d %d %d %d)"%(d, h, m, s))
print ' '.join(str(x) for x in v)