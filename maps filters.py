def square(x):
     return (x*x)
def iseven(x):
     return (x%2 ==0)
a=list(map(sqaure,filter(iseven,range(100)))
print a
