inp = input()
v = []
a = map(int, raw_input().split())
for i in a:
	c = 0
	while i != 1:
		if i%2 == 0:
			i = i/2 
			c += 1
		else:
			i = (i * 3) + 1
			c += 1
	v.append(c)
print ' '.join(str(x) for x in v)