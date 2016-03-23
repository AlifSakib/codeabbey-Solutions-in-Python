inp = input()
result = []
for i in range(inp):
	a, b = map(int, raw_input().split())
	sum = a + b
	result.append(sum)

print(' '.join(str(x) for x in result))