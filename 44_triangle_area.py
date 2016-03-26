from math import sqrt

v = []
def traingle(inp):
	for i in range(inp):
		x1, y1, x2, y2, x3, y3 = [int(x) for x in raw_input().split()]
		a = sqrt((x2 - x1)**2 + (y2 - y1)**2)
		b = sqrt((x3 - x1)**2 + (y3 - y1)**2)
		c = sqrt((x3 - x2)**2 + (y3 - y2)**2)
		s = (a + b + c) / 2
		area = sqrt(s * ((s - a) * (s - b) * (s - c)))
		v.append(str(area))
	print ' '.join(v)
traingle(input())