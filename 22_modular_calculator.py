s = input()
a = raw_input().split()
while a[0]!= '%':
	if a[0] == '+':
		s = s + int(a[1])
	if a[0] == '*':
		s = s * int(a[1])
	a = raw_input().split()
s = s % int(a[1])
print s