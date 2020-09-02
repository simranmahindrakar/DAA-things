for i in range(5):
    x=list(map(int,input().split()))
    l.append(x)
vertices=[]
for i in range(len(l)):
    vertices.append(l[i][0])
    vertices.append(l[i][1]
d={}
for i in d:
    if i in vertices:
        d[i].append(vertices[i][0])
    else:
        d[i]=l
print(d)
