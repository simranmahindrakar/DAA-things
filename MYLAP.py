def lapindrome(s):
    n=len(s)
    mid=len(s)//2
    if (len(s)%2==0):
        sl=s[:mid]
        sr=s[mid:]
        for i in range (len(sl)):
            if(sl.count(sl[i])!=sr.count(sl[i])):
                return "NO"
    else:
        sl=s[:mid]
        sr=s[mid+1:]
        for i in range(len(sl)):
            if(sl.count(sl[i])!=sr.count(sl[i])):
                return "NO"

    return "YES"
            
            
test=int(input())
d={}
for i in range(test):
    s=input()
    print(lapindrome(s))



