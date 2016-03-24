import string
exclude = set(string.punctuation)
inp = input()
v = []
for i in range(inp):
	a = raw_input().lower().replace(' ','')
	string = ''.join(ch for ch in a if ch not in exclude)
	reverse = string[::-1]
	if string == reverse:
		v.append('Y')
	else:
		v.append('N')
print ' '.join(str(x) for x in v)