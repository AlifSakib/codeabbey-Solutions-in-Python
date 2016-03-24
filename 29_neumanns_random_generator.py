inp = input()
a = raw_input().split()
v = []
for i in a:
	temp = []
	temp.append(i)
	count = 0
	new_num = int(i) * int(i)
	str_flag = True
	while str_flag:
		new_num = str(new_num)
		new_num = new_num.zfill(8)
		new_num = new_num[2:-2]
		if new_num not in temp:
			temp.append(new_num)
		else:
			str_flag = False
		new_num = int(new_num) * int(new_num)
		count += 1
	v.append(count)
print ' '.join(str(x) for x in v)