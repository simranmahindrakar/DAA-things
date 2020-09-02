v=[]
i = 1
while i:
    line = input()
    v.append(line)
    if line=='':
        break
    i = i+1
for i in range(len(v)//2,len(v)-1):
    print (v[i])
for j in range(0,len(v)//2):
    print(v[j])
