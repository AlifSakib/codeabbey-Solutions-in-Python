v = []
for i in range(input()):
	matches = raw_input().split()
	p1, p2 = 0, 0
	for match in matches:
		if any(match == x for x in ['RR','PP','SS']):
			0
		elif any(match == x for x in ['RS','SP','PR']):
			p1 += 1
		else:
			p2 += 1
	if p1 > p2:
		v.append('1')
	else:
		v.append('2')
print ' '.join(v)
