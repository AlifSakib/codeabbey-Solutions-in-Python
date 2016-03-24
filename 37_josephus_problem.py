N, K  = map(int, raw_input().split())
N = [e for e in range(1, N+1)]
count = 1
print N, K
while len(N) > 1:
	st = []
	for i in range(len(N)):
		if count % K == 0:
			print "continue"
		else:
			print "pass"
			print N[i]
		count += 1
		print count
	N -= 1
	print N
