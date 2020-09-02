def quicksort(a,l,r):
    if len(a)<=1:
        return 0
    green=l
    for blue in range(l,r-1):
        if(a[blue]<=a[7]):
            (a[green],a[blue])=(a[blue],a[green])
            green=green+1
    print(a)
