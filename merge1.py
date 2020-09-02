def merge(a,b):
    c=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    k=0
    while(k<m+n):
        if(j==n or (i<m and a[i][1]*b[j][0]>=b[j][1]*a[i][0])):
            c.append(a[i])
            i=i+1
            k=k+1
        else:
            c.append(b[j])
            j=j+1
            k=k+1
    return(c)
def mergesort(l):
    if len(l)<2:
          return l[:]
    mid=len(l)//2
    a=mergesort(l[:mid])
    b=mergesort(l[mid:])
    return merge(a,b)
N=int(input())
l=[]
for i in range(N):
    x=list(map(int,input().split()))
    l.append(x)
for i in range(N):
    l[i].append(i+1)
k=mergesort(l)
for i in range(len(k)):
    print(k[i][2])
