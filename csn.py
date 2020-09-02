n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
d={}
for i in ar:
    if i in d:
        d[i] +=1
    else:
        d[i]=1
l=list(d.values())
sorted(l)
print(max(l))
