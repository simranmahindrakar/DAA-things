def SelectionSort(A,n):
    for start in range(n):
        minpos=start
    for i in range(minpos+1,n):
        if(A[i] < A[minpos]):
           minpos=i
    (A[start],A[minpos])=(A[minpos],A[start])
    return A
A=[1,67,98,37,0,736,836,8737]
SelectionSort(A,len(A))

