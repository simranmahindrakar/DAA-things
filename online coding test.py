##def maxbad(l):
##  end = len(l) - 1
##  mymax = l[-1]
##  for i in range(end,0,-1):
##    if l[i] > mymax:
##       mymax = l[i]
##  return(mymax)

##def quicksortbad(l):
##  if len(l) < 2:
##    return(l)
##  else:
##    pivot = l[0]
##    smaller = [l[j] for j in range(1,len(l)) if l[j] < pivot]
##    bigger = [l[j] for j in range(1,len(l)) if l[j] > pivot]
##    rearrange = quicksortbad(smaller) + [pivot] + quicksortbad(bigger)
##    return(rearrange)


def min3(x,y,z):
    minimum=0
    if x <= y:
        if x <= z:
            minimum = x
    elif y<=z and y<x:
        minimum=y
    else:
        minimum=z
    return minimum

##def squarefree(n):
##    for i in range(2,n+1): #what if n itself is a square
##        if n%i**2==0:
##            return False
##    else:
##        return False

##def disjointlist(l1,l2):
##  for i in l1:
##    if i in l2:
##      return False
##  else:
##    return True

##v=[]
##i = 1
##while i:
##    line = input()
##    v.append(line)
##    if line=='':
##        break
##    i = i+1
##for i in range(len(v)//2,len(v)):
##    print (v[i])
##for j in range(0,len(v)//2-1):
##    print(v[j])


