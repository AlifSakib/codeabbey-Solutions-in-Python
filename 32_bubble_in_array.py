def checksum(a):
	result = 0
	for j in a:
		result += j
   		result = ( result * 113 ) % 10000007
	return result

def bubbleSort(a):
	a = a[:-1]
	sorted = False
	swap_count = 0
	while not sorted:
		sorted = True
		for i in range(len(a)-1):
			if a[i] > a[i+1]:
				sorted = True
				swap_count += 1
				a[i], a[i+1] = a[i+1], a[i]
	check = checksum(a)
	print swap_count, check

bubbleSort([int(x) for x in raw_input().split()])
