#counting sort
def count_keys_eq(a,n,m):
    equal=[0]*m
    for i in range(len(a)):
        key=a[i]
        equal[key]=equal[key]+1
    return equal
def count_keys_less(equal,m):
    less=[0]*m
    for j in range(len(less)):
        less[j]=less[j-1]+equal[j-1]
    return less
def count2_sort(less):
    b=[0]*len(a)
    c=[0]*m
    for j in range(len(c)):
        c[j]=less[j]+1
    for i in range(len(a),-1,-1):
        key=a[i]
        index=equal[key]
        b[index]=a[i]
        c[key]=c[key]+1
    return b
def count_sort(a,n,m):
    count_keys_eq(a,n,m)
    count_keys_less(equal,m)
    k=count2_sort(less)
    return k
    
    
