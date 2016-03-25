def decipher(a, k):
	array = []
	k = 26 - k
	for i in range(len(a)):
		rep = k
		od = ord(a[i])
		if od in range(65,91):
			while rep > 0:
				od += 1
				if od == 91:
					od = 65
				rep -= 1
			array.append(chr(od))
		else:
			array.append(a[i])
	p = ''.join(str(x) for x in array)
	return p +'.'

inp = map(int, raw_input().split())
k = inp[1]
v = []
for i in range(inp[0]):
	a = raw_input()
	a = a[:-1].upper()
	c = decipher(a, k)
	v.append(c)
print ' '.join(str(e) for e in v)