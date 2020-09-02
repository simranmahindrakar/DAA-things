l=[]
for i in range(5):
    x=list(map(int,input().split()))
    l.append(x)
d={}
for i in range(len(l)):
    if l[i][0] in d:
        d[i].append(l[i][1])
        d[i].append(l[i][2])
    else:
        d[i]=l[i][0]
