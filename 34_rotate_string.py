inp = input()
v = []
for i in range(inp):
	a = raw_input().split()
	k = int(a[0])
	s = a[1]
	if k < 0:
		while k < 0:
			k += 1
			temp = s[len(s)-1] + s[0:-1]
			s = temp
		v.append(s)
	else: 
		while k > 0:
			k -= 1
			temp = s[1:] + s[0]
			s = temp
		v.append(s)
print ' '.join(str(x) for x in v)