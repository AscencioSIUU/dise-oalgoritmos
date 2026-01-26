def insertion_sort(A):
    for j in range(1,len(A)):
        k=A[j]
        i=j-1
        while i>=0 and A[i]>k:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=k
