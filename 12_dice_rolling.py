import math, random
inp = input()
v = []
for i in range(inp):
	a = raw_input()
	a = float(a)
	a = a * 6
	a = int(math.floor(a))+1
	v.append(a)

print ' '.join(str(x) for x in v)