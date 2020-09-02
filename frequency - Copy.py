def frequency(l):
    d={}
    for i in l:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    sfrq=[]
    l=list(sorted(d.values()))
    m=max(l)
    n=min(l)
    maxfr=[]
    minfr=[]
    for i in d:
        if d[i]==n:
            minfr.append(i)
        if d[i]==m:
            maxfr.append(i)
    t=(sorted(minfr),sorted(maxfr))
    return t
    
            
        
##    k=mergesort(sfrq)
##    return k
##def merge(a,b):
##    m=len(a)
##    n=len(b)
##    c=[]
##    i=0
##    j=0
##    k=0
##    while(k<m+n):
##        if(j==n or (i<m and a[i]<b[j])):
##           c.append(a[i])
##           i=i+1
##           k=k+1
##        elif(i==m or a[i]>b[j]):
##           c.append(b[j])
##           j=j+1
##           k=k+1
##    print(c)
##def mergesort(sfrq):
##    if len(sfrq)<2:
##        return sfrq[:]
##    mid=len(sfrq)//2
##    a=mergesort(sfrq[:mid])
##    b=mergesort(sfrq[mid:])
##    return merge(a,b)
