n, k = map(int, raw_input().split())
N = [x for x in range(1,n+1)]
count = 1
while len(N) > 1:
	st = []
	l = []
	for i in range(len(N)):
		if count % k == 0:
			l.append(N[i])
		else:
			st.append(N[i])
		count += 1
	N = st[:]
print N[0]