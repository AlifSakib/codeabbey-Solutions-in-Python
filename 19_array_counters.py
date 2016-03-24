l, inp = map(int, raw_input().split())
a = map(int, raw_input().split()[:l])
v = []
for i in range(1,inp+1):
	v.append(a.count(i))
print ' '.join(str(x) for x in v)

