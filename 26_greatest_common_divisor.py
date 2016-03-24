def gcd(a, b):
	m1, m2 = max(a, b), min(a, b)
	while a != b:
		a, b = m1 - m2, m2
		m1, m2 = max(a, b), min(a, b)
	return a

def lcm(a, b, m):
	return int(a*b/m)
v = []	
inp = input()
for i in range(inp):
	a, b = map(int, raw_input().split())
	m = gcd(a, b)
	l = lcm(a, b, m)
	s = '(' + str(m) + ' ' + str(l) + ')'
	v.append(s)
print ' '.join(str(x) for x in v)