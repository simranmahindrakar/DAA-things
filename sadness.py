def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if(l<n and arr[i][2]<arr[l][2]):
        largest=l
    if(r<n and arr[i][2]<arr[r][2]):
        largest=r
    if (largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
    heapify(arr,n,largest)



def heapsort(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,-1,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr

test=int(input())
for i in range(test):
    n=[]
    x=list(map(int,input().split()))
    for i in range(x[0]):
        n.append(list(map(int,input().split())))
    k=heapsort(n)
    print(k)
