##N=input("enter no")
##l=[]
##N=int(N)
##for i in range(N):
##    x=list(map(int,input().split()))
##    l.append(x)
##for i in range(len(l)):
##    l[i].append(i+1)
##for j in range(len(l)):
##    pos=j
##    while(pos>0 and l[pos][1]*l[pos-1][0]>l[pos][0]*l[pos-1][1]):
##        (l[pos],l[pos-1])=(l[pos-1],l[pos])
##        pos=pos-1
##for i in range(len(l)):
##    print(l[i][2])
##


N=input()
l=[]
N=int(N)
for i in range(N):
    x=list(map(int,input().split()))
    l.append(x)
for i in range(len(l)):
    l[i].append(i+1)
k=mergesort(l)
for i in range(k):
    print(k[i][2]
def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j,k)=(0,0,0)
    while(k<m+n):
        if(j==n or (i<m and a[i][1]*b[j][0]>a[i][0]*b[j][1])):
            c.append(a[i])
            i=i+1
            k=k+1
        elif(i==m or a[i][1]*b[j][0]<a[i][0]*b[j][1]):
            c.append(b[j])
            j=j+1
            k=k+1
def mergesort(l):
    if len(l)<2:
          return l[:]
    mid=len(l)//2
    a=mergesort(l[:mid])
    b=mergesort(l[mid:])
    return merge(a,b)


##N=input()
##l=[]
##N=int(N)
##for i in range(N):
##    x=list(map(int,input().split()))
##    l.append(x)
##for i in range(len(l)):
##    l[i].append(i+1)
##def mergesort(l): 
##    mid=len(l)//2
##    a=mergesort(l[:mid])
##    b=mergesort(l[mid:])
##    return merge(a,b)
##def merge(a,b):
##    (c,m,n)=([],len(a),len(b))
##    (i,j,k)=(0,0,0)
##    while(k<m+n):
##        if(j==n or a[i][1]*a[i-1][0]>b[j][0]*b[j-1][1]):
##            c.append(a[i])
##            i=i+1
##            k=k+1
##        elif(i==m or a[i][1]*a[i-1][0]<b[j][0]*b[j-i][1]):
##            c.append(b[j])
##            j=j+i
##            k=k+1
##    for i in range(len(c)):
##        print(c[i][2])


