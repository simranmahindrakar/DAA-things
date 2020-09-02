##def max3bad(x,y,z):
##  maximum = 0
##  if x >= y:
##    if x >= z:
##      maximum = x
##  elif y >= z:
##    maximum = y
##  else:
##    maximum = z
##  return(maximum)

##def perfect(n):
##  sum=0
##  for i in range(1,n):
##    if(n%i==0):
##      sum=sum+i
##  if sum==n:
##      return True
##  else:
##      return False
      
##def secondmax(l):
##  (mymax,mysecondmax) = (0,0)
##  for i in range(len(l)):
##      if l[i]>mymax:
##          mymax,mysecondmax=l[i],mymax
##      elif mymax>l[i]>mysecondmax:
##          mysecondmax=l[i]
##  return (mysecondmax)
##
##
##def second_largest(numbers):
##    first, second = 0,0
##    for n in numbers:
##        if n > first:
##            first, second = n, first
##        elif first > n > second:
##            second = n
##    return second


##def repeated(l):
##    d={}
##    for i in l:
##        if i in d:
##            d[i]=d[i]+1
##        else:
##            d[i]=1
##    count=0
##    for j in d.values():
##        if j>1:
##            count+=1
##    return(count)

##def sublist(l1,l2):
##    for i in l1:
##        if i in l2 and l1[i]==l2[i]:
##            return True
##        else:
##            return False
##

#print every 3rd line of text
##i = 1
##while i:
##    line = input()
##    if line=='':
##        break
##    if i%3 == 0:
##        print(line)
##    i = i+1

##def square(x):
##    return (x*x)
##def iseven(x):
##    return (x%2==0)
##k=list(map(square,filter(iseven,range(100))))
##sum=0
##for i in k:
##    sum=sum+i
##print (sum)

def square(x):
    return (x*x)
def iseven(x):
    return (x%2==0)
p=[square(x) for x in range(100) if iseven(x)]


