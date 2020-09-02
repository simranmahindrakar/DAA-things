def merge(a,b):
    c=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    k=0
    while(k<m+n):
        if(j==n or (i<m and a[i][1]<b[j][1])):
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
    mid=len(l)//2
    a=mergesort(l[:mid])
    b=mergesort(l[mid:])
    return merge(a,b)

#taking input
N=int(input())
l=[]
for i in range(N):
    x=list(map(int,input().split()))
    l.append(x)
for j in range(len(l)):
    l[j][1]=l[j][0]+l[j][1]-1

k=mergesort(l) #calling mergesort

for i in range(len(k)):
    k[i].append(i+1) #renumbering the sorted list


start_time=[]#array containing start times
for i in range(len(k)):
    start_time.append([]) 
for i in range(len(k)):
    start_time[i].append(k[i][0])
    start_time[i].append(k[i][2])

v=[] #list containing selected intervals
i=0
v.append(k[i][2]) #first interval will always be taken
for q in range(len(start_time)):
    if start_time[q][0]>=k[i][1]:
        v.append(start_time[q][1])
        i=q
print(len(v))



