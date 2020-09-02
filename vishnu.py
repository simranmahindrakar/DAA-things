def merge(a,b): # this is the merge function
    m=len(a)
    n=len(b)
    c=[]
    i=0
    j=0
    k=0
    while(k<m+n):
        if(j==n or (i<m and a[i][1]*b[j][0]>b[j][1]*a[i][0])):
            c.append(a[i])
            i=i+1
            k=k+1
        else: #elif (i==m or a[i]>b[j]): NOT required
            c.append(b[j])
            j=j+1
            k=k+1
    return(c)

def sim_orig_sort(l): # this is the merge sort funxn
    if len(l)<2:
        return l[:]
    
    mid=len(l)//2
    a=sim_orig_sort(l[:mid])
    b=sim_orig_sort(l[mid:])
    return merge(a,b)

def simshoemerge() : #This is the main program 
    item =[]
    N=int(input())
    for i in range (N) :
        new = list(map(int, input().split()))
        item.append(new)
    for i in range (N):
        item[i].append(i+1)
    k=sim_orig_sort(item)
    for i in range(len(k)):
        print(k[i][2])
