inp = input()
result = []
for i in range(inp):
	a = map(int, raw_input().split())
	min_value = min(a)
	result.append(min_value)

print(' '.join(str(x) for x in result))