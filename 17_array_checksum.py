inp = input()
a = map(int, raw_input().split()[:inp])
result = 0
for j in a:
   result += j
   result = ( result * 113 ) % 10000007
print result