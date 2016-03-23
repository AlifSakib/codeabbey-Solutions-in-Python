a = raw_input().split()
inp = a[0]
inp_list = a[1:len(a)]
v = []
for i in inp_list:
    c = int(round((int(i)-32)/1.8))
    v.append(c)
print ' '.join(str(x) for x in v)