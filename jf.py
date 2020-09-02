sc_de=list(map(int,input().split())) #sc_de[0]=source [1]=destination
nm=list(map(int,input().split())) #nm[0]=nodes
greenflash=list(map(int,input().split()))
l=[]
for i in range(nm[1]):
    x=list(map(int,input().split()))
    l.append(x)#l[i][0]=start l[i][1]=end l[i][2]=edge weight
#visited=[]
for j in range(len(l)):
    #visited[j][0]==False and visited[j][1]==False
    l[j][0]=10000
    l[j][1]=10000
def heapify(l):
    for i in range(len(l)//2,0,-1):
        min_heap(l,n,i)
    for i in range(n-1,0,-1):
        l[i][2],l[0][2]=l[0][2],l[i][2]
        min_heap(l,i,l[0][2])
    
def min_heap(l,n,i):
    smallest=i
    l=2*i+1
    r=2*i+2
    if l<n and l[i][2]>l[l][2]:
        smallest=l
    elif r<n and l[i][2]>l[r][2]:
        smallest=r
    if smallest!=i:
        (l[i],l[smallest])=(l[smallest],l[i])
    min_heap(l,n,smallest)
