def substrings(s):
    l=len(s)
    for end in range(l,0,-1):
        for i in range(l-end+1):
            yield s[i:i+end]

def palindrome(s):
    return s==s[::-1]

def bleh(s):
    for l in substrings(s):
        if palindrome(l):
            return(l)
n=input()
s=input()
k=bleh(s)
print(len(k))
print(k)
