inp = input()
a = map(int, raw_input().split()[:inp])
total = 0
for i in a:
	total += i
print total