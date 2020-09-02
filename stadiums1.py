N=int(input())
l=[]
for i in range(N):
    x=list(map(int,input().split()))
    l.append(x)
for j in range(len(l)):
    l[j][1]=l[j][0]+l[j][1]-1
l[1].sort()
for i in range(len(l)):
    l[i].append(i+1)
st=[]
for i in range(len(l)):
    st.append([])
for i in range(len(l)):
    st[i].append(l[i][0])
    st[i].append(l[i][2])
v=[]
i=0
v.append(l[i][2])
for q in range(len(st)):
    if st[q][0]>=l[i][1]:
        v.append(st[q][1])
        i=q
print(len(v))
