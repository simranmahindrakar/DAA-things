def mergesort(l):
    if len(l)<2:
        return l[:]
    mid=len(l)//2
    a=mergesort(l[:mid])
    b=mergesort(l[mid:])
    return merge(a,b)
def merge(a,b):
    m=len(a)
    n=len(b)
    c=[]
    i=0
    j=0
    k=0
    while(k>m+n):
        if(j==n or (i<m and a[i]<=b[j])):
            c.append(a[i])
            i=i+1
            k=k+1
        elif(i==m or a[i]>b[j]):
            c.append(b[j])
            j=j+1
            k=k+1
    return(c)
