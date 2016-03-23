inp = input()
v = []
a=0;e=0;i=0;i=0;o=0;u=0;y=0

for i in range(inp):
    st = raw_input()
    a = st.count('a')
    e = st.count('e')
    i = st.count('i')
    o = st.count('o')
    u = st.count('u')
    y = st.count('y')
    v.append(a+e+i+o+u+y)
print(" ".join(str(e) for e in v ))