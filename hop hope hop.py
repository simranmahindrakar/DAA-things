##def onehop(l):
##    k=[]
##    for i in l:
##        for j in l:
##            if i[0]==j[1] and i[1]!=j[0]:
##                k.append(i)
##    print(k)
def onehop(l):
  hopstop=[]

  for i in l :
    for j in range(len(l)):
     if i[0]==l[j][1] and i[0] not in hopstop:
        hopstop.append(i[0])
        break  
    
  
  r=[]
  for i in hopstop:
    for j in l :
      if j[0]==i:
        for k in l:
          if k[1]==i and j[1]!=k[0] and (k[0],j[1]) not in r:  
            r.append((k[0],j[1]))
          
  
  return (sorted(r))
 
