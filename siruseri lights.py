class Queue:
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
	
    def dequeue(self):
        return self.items.pop()
	
    def size(self):
        return len(self.items)
q=Queue()
for i in l:
    q.enqueue(i)
while q.isEmpty()==False:
     
    
##heapify---------------------------------------------
def min_heap(queue,n,sc_de[0]):
    smallest=i
    l=2i+1
    r=2i+2
    if l<n and queue[i][2]>queue[l][2]:
        smallest=l
    elif r<n and queue[i][2]>queue[r][2]:
        smallest=r
    if smallest!=i:
        (queue[i],queue[smallest])=(queue[smallest],queue[i])
    min_heap(queue,n,smallest)
def heapify(l,n,

##take input---------------------------------------------------
sc_de=list(map(int,input().split())) #sc_de[0]=source [1]=destination
nm=list(map(int,input().split())) #nm[0]=nodes
greenflash=list(map(int,input().split()))
l=[]
for i in range(nm[1]):
    x=list(map(int,input().split()))
    l.append(x)#l[i][0]=start l[i][1]=end l[i][2]=edge weight
for j in range(len(l)):
    l[j][0]=10000
    l[j][1]=10000
sc_de[0]=0
##time=[]
##for i in range(len(l)):
##    time.append(l[i][2])
##vertices=[]
##for i in range(len(l)):
##    vertices.append(l[i][0])
##    vertices.append(l[i][1]

##print(nm)
##print(greenflash)
##print(l)
##print(time)
#print(vertices)
