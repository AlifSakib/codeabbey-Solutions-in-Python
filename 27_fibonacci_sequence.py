no = input()
dic = {}
dic[0]=0
dic[1]=1
for i in range(2,1000):
    dic[i]=dic[i-1]+dic[i-2]
new_value = []
for i in range(no):
    a = raw_input()
    a = int(a)
    for k,v in dic.items():
        if(a==v):
            new_value.append(k)

print(' '.join((str(e)) for e in new_value))