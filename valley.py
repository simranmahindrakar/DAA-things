def valley(l):
    track=0
    if len(l)<3:
        return False
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            track=1
    if track==1:
        return True
    else:
        return False

