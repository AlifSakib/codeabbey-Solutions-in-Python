no = input()
a = []
for i in range(no):
    l = map(int, raw_input().split())
    total=0
    for c in l:
        if c == 0:
            break
        else:
            total = total + c
    avg =float(total)/float(len(l)-1)
    avg = round(avg)
    a.append(int(avg))
print(" ".join((str(e)) for e in a))
