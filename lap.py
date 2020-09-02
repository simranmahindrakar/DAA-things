def palindrome(s):
    ind=len(s)//2
    if len(s)%2==0:
        sl=s[:ind]
        sr=s[ind:]
        for i in range(len(sl)):
            if sl.count(sl[i])!=sr.count(sl[i]):
                return "NO"
    else:
        sl = s[:ind]
        sr = s[ind+1:]
        for i in range(len(sl)):
            if sl.count(sl[i]) != sr.count(sl[i]):
                return "NO"
    return "YES"
 
 
t = int(input())
for _ in range(t):
    s = input()
    print(palindrome(s))
 
def lap(a,b):
	al=len(a)
	bl=len(b)
	if al!=bl:
			return "NO"
 
	for i in a:
		
		if a.count(i)!=b.count(i):
			return "NO"
	return 'YES'
 
 
 
 
n=int(input())
for _ in range(n):
	l=[x for y in input() for x in y]
 
	if len(l)%2==0:
		a=l[0:len(l)//2]
		b=l[len(l)//2:]
		print(lap(a,b))
	else:
		a=l[0:len(l)//2]
		b=l[len(l)//2+1:]
		print(lap(a,b)) 
