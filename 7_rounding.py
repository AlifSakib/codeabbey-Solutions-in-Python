result = []
inp = input()
for i in range(inp):
	a, b = map(float, raw_input().split())
	temp = int(round(a/b))
	result.append(temp)

print ' '.join(str(x) for x in result) 