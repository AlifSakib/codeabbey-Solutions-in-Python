inp = input()
v = []
for i in range(inp):
	a = map(int, raw_input().split())
	a.sort()
	if (a[0]**2) + (a[1]**2) == (a[2]**2):
		v.append("R")
	elif (a[0]**2) + (a[1]**2) > (a[2]**2):
		v.append("A")
	else:
		v.append("O")
print ' '.join(str(x) for x in v)	