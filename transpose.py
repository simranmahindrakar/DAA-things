def transpose(m):
    result=[]
    for i in range(len(m[0])):
        result.append([])
    num_col=len(m[0])
    num_row=len(m)
    for c in range(num_col):
        for r in range(num_row):
            result[c].append(m[r][c])
    return(result)
