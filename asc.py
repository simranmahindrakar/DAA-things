def ascending(l):
    if len(l)==0 or len(l)==1:
        return True
    for i in range(1,len(l)):
        if l[i-1]>l[i]:
            return False
    return True

