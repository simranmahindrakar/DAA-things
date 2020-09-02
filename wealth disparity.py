##N=int(input())
##l=[]
##for i in range(N):
##    l.append([])
##x=list(map(int,input().split()))
##y=list(map(int,input().split()))
##for i in range(len(x)):
##    l[i].append(x[i])
##for i in range(len(x)):
##    l[i].append(y[i])
##visited=[]
##for i in range(len(l)):
##    visited[i]=0
##for j in range(len(l)):
##    def dfs(j):
##        visited[j]=

#1 8 4 ,8 4 4 4 9
l=[5,7,5,7,5,7,5,7,1,8,4,1,8,4,1,8,4,4,4,4,9]
d={}
for i in l:
    d[i]=0
for i in l:
    d[i]=d[i]+1
print(d)
