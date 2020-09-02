def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j,k)=(0,0,0)
    while(k<m+n):
        if(j==n or a[i][1]*b[j][0]>a[i][0]*b[j][1]):
            c.append(a[i])
            i=i+1
            k=k+1
        elif(i==m or a[i][1]*b[j][0]<a[i][0]*b[j][1]):
            c.append(b[j])
            j=j+1
            k=k+1
    return c
def mergesort(l): 
    mid=len(l)//2
    a=mergesort(l[:mid])
    b=mergesort(l[mid:])
    return merge(a,b)
