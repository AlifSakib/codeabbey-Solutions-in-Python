inp = input()
a = raw_input().split()
a = map(float, a)
v = []
v.append(a[0])
for i in range(1, len(a)-1):
	v.append((a[i-1] + a[i] + a[i+1]) / 3.0)
v.append(a[len(a)-1])
print ' '.join(str(x) for x in v)