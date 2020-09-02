#####quicksort
##def quicksort(A,l,r):
##    if (r-l <=1): #base case
##        return 0
##    blue=r-1
##    for green in range (r-1,0,-1):
##        if A[green]>=A[r]:
##            (A[green],A[blue])=(A[blue],A[green])
##            blue=blue-1
##    #swap pivot
##    (A[r],A[blue-1])=(A[blue-1],A[r])
##    print(A)
##    quicksort(A,l,green)
##    quicksort(A,green+1,r)
##    return A

##print("hello",end=" ")
##print("world,wol,fj")
##print("yay")
##x=10
##print("the value of x is",x,sep
##
##def quicksort(A,l,r):
##    if(r-l<=1):
##        return 0
##    green=l
##    for blue in range(l,7):
##        if(A[blue]<=A[7]):
##            (A[green],A[blue])=(A[blue],A[green])
##            green=green+1
##    (A[7],A[green+1])=(A[green+1],A[7])
##    print (A)
##
##
##    

def quicksort(A):
    r=A[7]
    if(len(A)<=1):
        return 0
    green=0
    for blue in range(0,len(A)-1):
        if(A[blue]<=r):
            (A[green],A[blue])=(A[blue],A[green])
    (r,A[green+1])=(A[green+1],r)
    print(A)
            
