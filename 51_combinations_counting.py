def fact(n):
	if n==0 or n ==1:
		return 1
	else:
		return n * fact(n-1)

def combination(n, k):
	return (fact(n)/(fact(k) * fact(n-k)))

v = []
for i in range(input()):
	n, k = map(int, raw_input().split())
	v.append(str(combination(n, k)))

print ' '.join(v)	