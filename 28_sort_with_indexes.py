inp = input()
v = []
a = raw_input().split()
b = a
a = map(int, a)
a.sort()
for i in a:
	c = b.index(str(i))
	v.append(c+1)
print ' '.join(str(x) for x in v)