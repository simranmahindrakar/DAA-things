def ascending(l):
    if(len(l)==0 or len(l)==1):
        return True
    for i in range(len(l)):
        pos=i
        while(pos>0 and l[pos]>=l[pos-1]):
            return True
            pos=pos-1
    else:
        return False
