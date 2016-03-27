number, guess = raw_input().split()
a = raw_input().split()
v = []
for i in a:
	c1, c2 = 0, 0 
	count1, count2 = [], []
	count1 = [c1 + 1 for j in range(len(i)) if i[j] == number[j]]
	count2 = [c2 + 1 for j in range(len(i)) if i[j] in number and i[j] != number[j]]
	s = str(len(count1)) + '-' + str(len(count2))
	v.append(s)
print ' '.join(v)