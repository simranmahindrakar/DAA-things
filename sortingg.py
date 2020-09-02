def merge(a,b):
    
    m=len(a)
    n=len(b)
    i=0
    j=0
    k=0
    while(k<m+n):
        if(j==n or a[i]<=b[j]):
            c.append(a[i])
            k=k+1
            i=i+1
        if(i==m or a[i]>b[j]):
            c.append(b[j])
            k=k+1
            j=j+1
    return c
##def mergesort(x):
##    if(len(x)==1):
##        return x
##    mid=len(x)//2
##    a=mergersort(x[:mid])
##    b=mergesort(x[mid:])
##    return merge(a,b)
            
            
