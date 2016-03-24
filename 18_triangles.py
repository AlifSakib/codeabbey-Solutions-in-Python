def isTriangle(a):
	s1, s2, s3 = a[0], a[1], a[2]
	if (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2):
		return '1'
	else:
		return '0'

inp = input()
v= []
for i in range(inp):
	a = map(int, raw_input().split())
	res = isTriangle(a)
	v.append(res)
print ' '.join(str(x) for x in v)