inp = input()
v = []
a = raw_input().split()[:inp]
for j in a:
	sum = 0
	k = 1
	for i in j:
		sum += int(i) * k
		k += 1
	v.append(sum)

print ' '.join(str(x) for x in v)