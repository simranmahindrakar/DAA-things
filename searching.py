##
##def linsearch(A,n,x):
##    if (n==0 or n==1):
##        return -1
##    for i in range(0,n):
##        if A[i] == x:
##            return i
##    else:
##        return -1


##def sls(A,n,x):
##    last=A[n-1]
##    A[n-1]=x
##    i=0
##    while(A[i]!=x):
##        i=i+1
##    A[n-1]=last
##    if(i<n and A[i]==x):
##        return i
##    elif(A[n-1]==x):
##        return n-1
##    else:
##        return -1

def depth(s):
    count=0
    for j in range(0,len(s)):
        if (s[j] == ')'):
            count=count+1
    return count

##def depth(s):
##    count=0
##    for j in range(0,len(s)):
##        if ((s[j] == '(') and (s[j] != ')')):
##          count=count+1
##    return count
## 
