inp = input()
a = map(int, raw_input().split()[:inp])
sorted = False
array_pass, array_swap =0, 0
while not sorted:
	sorted = True
	for i in range(len(a)-1):
		if a[i] > a[i+1]:
			array_swap += 1
			a[i], a[i+1] = a[i+1], a[i]
			sorted = False
	array_pass += 1
print array_pass, array_swap