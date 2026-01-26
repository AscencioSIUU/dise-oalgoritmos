from math import floor

def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = (n1+1)*[None]
    R = (n2+1)*[None]
    for i in range(n1):
        L[i]=A[p+i]
    for j in range(n2):
        R[j]=A[q+1+j]
    L[n1]=float('inf')
    R[n2]=float('inf')
    #print('mergemergemergemerge')
    #print(L)
    #print(R)
    #print('mergemergemergemerge')
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<= R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1

def merge_sort(A,p,r):
    #print(p)
    #print(r)
    #print('---')
    if p<r:
        q=int(floor((p+r)/2))
        #print(q)
        #print('***')
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
        #print(A)
        #print('+++')
