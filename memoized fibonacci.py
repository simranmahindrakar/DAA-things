###memoization approach
##def fib(n):
##    fibtable={}
##    if n in fibtable:
##        return (fibtable[n]) 
##    if n==1 or n==0:
##        value=n
##    else:
##        value=fib(n-1)+fib(n-2)
##    fibtable[n]=value
##    return(value)
##
##
##dynamic fib
##bottom up approach
##
##def fib(n):
##    fibtable={} #empty dictionary
##    fibtable[0]=0
##    fibtable[1]=1
##    for i in range(2,n+1):
##        fibtable[i]=fibtable[i-1]+fibtable[i-2]
##    return(fibtable[n])


def fib(a,b,n):
    fibtable={} #empty dictionary
    fibtable[0]=a
    fibtable[1]=b
    for i in range(2,n+1):
        fibtable[i]=fibtable[i-1]**2+fibtable[i-2]
    return(fibtable[i-1])




x=list(map(int,input().split()))
f=fib(x[0],x[1],x[2])
print(f)



