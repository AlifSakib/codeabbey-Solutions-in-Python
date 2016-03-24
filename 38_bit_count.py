inp = input()
v = []
a = map(int, raw_input().split())
for i in a:
	val = format(i & 0xffffffff, '32b')
	v.append(str(val).count('1'))
print ' '.join(str(x) for x in v)