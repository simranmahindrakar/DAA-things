def bracket(s):
    n=len(s)
    count=0
    record=0
    for i in range(n):
        if s[i]=='<':
            count=count+1
            if(record<count):
                record=count
        else:
            count=count-1
    if(record>0):
        return record
    else:
        return 0
test=int(input())
for i in range(test):
    s=input()
    print(bracket(s))
    
            
            
            
