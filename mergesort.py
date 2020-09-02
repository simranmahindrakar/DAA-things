def merge(a,b):
    m=len(a)
    n=len(b)
    c=[]
    i=0
    j=0
    k=0
    while(k<m+n):
        if(j==n or a[i]<b[j]):
            c.append(a[i])
            i=i+1
            k=k+1
        else:
            c.append(b[j])
            j=j+1
            k=k+1
    return (c)
            
def mergesort(l):
    if len(l)<2:
        return l[:]
    mid=len(l)//2;
    a=mergersort(l[:mid])
    b=mergesort(l[mid:])

    return merge(a,b)
n=int(input())
l=[]
for i in range(0,n+1):
    l.append(input())
k=mergesort(l)
for i in k:
    print (k)

    
