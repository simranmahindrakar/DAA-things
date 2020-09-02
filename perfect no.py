def perfect(n):
    fn=[]
    sum=0
    for i in range(1,n):
        if(n%i == 0):
            fn.append(i)
    for j in fn:
        sum=sum+j
    if(sum == n):
        return True
    else:
        return False
