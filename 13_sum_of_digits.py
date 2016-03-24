inp = input()
v = []
for i in range(inp):
	a = map(int, raw_input().split())
	sum = str((a[0] * a[1]) + a[2])
	res = 0
	for j in sum:
		res += int(j)
	v.append(res)

print ' '.join(str(x) for x in v)