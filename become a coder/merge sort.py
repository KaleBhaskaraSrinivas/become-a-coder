def merge(data,L,M,H):
    n=M-L+1# size of list a
    m=H-M# size of b
    a=[0]*n
    b=[0]*m
    for i in range(n):
        a[i]=data[L+i]
    
    for i in range(m):
        b[i]=data[M+i+1]
    i=0
    j=0
    k=L
    while i<n and j<m:
        if a[i]<=b[j]:
            data[k]=a[i]
            i+=1
            k+=1
        else:
            data[k]=b[j]
            j+=1
            k+=1
    while i<n:
        data[k]=a[i]
        i+=1
        k+=1
    while j<m:
        data[k]=b[j]
        j+=1
        k+=1
    #print(*a)
    #print(*b)
    
        
def mergesort(data,L,H):
    if L<H:
        M=(H+L)//2
        mergesort(data,L,M)
        mergesort(data,M+1,H)
        merge(data,L,M,H)
        #print(data)

H=int(input())
data=list(map(int,input().split()))
mergesort(data,0,H-1)
print(*data)



"""

1. 2 sorted arrays then merge
2. take 1 array with parts
3. apply merge sort
8
0   1  2  3  4 5  6  7
11 10 20 30 40 2 11 12
L        M          H


10 11 20 30

        
10 11






    c=[0]*(m+n)
    i=0
    j=0
    k=0
    while i<m and j<n:
        if a[i]<=b[j]:
            c[k]=a[i]
            i+=1
            k+=1
        else:
            c[k]=b[j]
            j+=1
            k+=1
    while i<m:
        c[k]=a[i]
        i+=1
        k+=1
    while j<n:
        c[k]=b[j]
        j+=1
        k+=1 
    return c














"""
