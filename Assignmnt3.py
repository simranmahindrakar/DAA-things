##def ascending(l):
##    if len(l)==0 or len(l)==1:
##        return True
##    for i in range(1,len(l)):
##        if l[i-1]>l[i]:
##            return False
##    return True

####
##def valley(l):
##    track=0
##    if len(l)<3 or l[0]<l[1]:
##        return False
##    for i in range(1,len(l)):
##        if(l[i-1]<l[i]):
##            pos=i
##            break
##        if l[i-1]==l[i]:
##            return False
##    else:
##        return False
##    for i in range(pos,len(l)):
##        if l[i-1]>l[i]:
##            return False
##    return True
####            

##def valley(list):
##  if(len(list)==0):
##    return(True)
##  if(len(list)==1):
##    return(False)
##  if(list[0]<list[1]):
##    return(False)
##  for i in range(0,len(list)-1):
##    if(list[i]<list[i+1]):
##      pos=i
##      break
##    if(list[i]==list[i+1]):
##      return(False) 
##  else:
##    return(False)
##  for i in range(pos,len(list)-1):
##    if(list[i]>=list[i+1]):
##      return(False)
##  return(True)
  
##def transpose(m):
##    result=[0]*len(m[0])
##
##    for c in range(num_col):
##        for r in range(num_row):
##            result[c][r]=m[r][c]
##    return result
##
##
##
def transpose(m):
    result=[]
    for i in range(len(m)):
        for j in range(len(m[0])):
            result
    return result
##matrix = [[1, 2],
##	  [3, 4],
##	  [5, 6]]
##rmatrix = [[0, 0, 0],
##	   [0, 0, 0]]
##for i in range(len(matrix)):
##	for j in range(len(matrix[0])):
##		rmatrix[j][i] = matrix[i][j]
##
##		
##for r in rmatrix:
##	print(r)
