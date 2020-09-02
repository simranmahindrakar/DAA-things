##def ascending(l):
##    if(len(l)==0 or len(l)==1):
##        return True
##    for i in range(len(l)):
##        pos=i
##        while(pos>0 and l[pos]>=l[pos-1]):
##            return True
##            pos=pos-1
##    else:
##        return False

##
##def mystery(l):
##    l = l[2:5]
##    return()
##list1 = [7,82,44,23,11]
##mystery(list1)
##print (list1)

##def mystery(l):
##    if len(l) < 2:
##        return (l)
##    else:
####        return ([l[-1]] + mystery(l[1:-1]) + [l[0]])
##triples = [ (x,y,z) for x in range(1,4) for y in range(2,5) for z in range(5,8) if x+y > z ]


##runs = {"Test":{"Dhawan":[190,14,35,119],"Kohli":[3,103,13,42],"Pujara":[153,15,133,8]},"ODI":{"Dhawan":[37],"Kohli":[63]}}
###runs["ODI"]["Pujara"].extend([44])
###runs["ODI"]["Pujara"][0]=44
##runs["ODI"]["Pujara"]=[44]


inventory={}
inventory[("Amul","Mystic Mocha")] = 55
##inventory[["Amul","Mystic Mocha"]] = 55
inventory["Amul, Mystic Mocha"] = 55
inventory["Amul"] = ["Mystic Mocha",55]
