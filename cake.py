test=int(input())
for i in range(test):
    s=[]
    types=int(input())
    for j in range(types):
        f=input()
        s.append(f)
    if(("cakewalk" in s) and ("simple" in s) and ("easy" in s) and(("easy-medium" in s) or ("medium" in s)) and (("medium-hard" in s) or ("hard" in s))):
        print("yes")
    else:
        print("no")
    





