"""
0  1 2 3 4  5  6  7  8  9
6 2 9 8 3  10  15  12 16 14


0 1 2 3 4
6 2 9 8 3 

"""

def qsort(data,l,h):#l=0 h=9
    if l<h:
        pe=l
        i=l+1
        j=h
        while i<=j:
            while i<=j and data[i]<data[pe]:
                i+=1
            while i<=j and data[j]>=data[pe]:
                j-=1
            if i<=j:
                data[i],data[j]=data[j],data[i]
        data[pe],data[j]=data[j],data[pe]
        qsort(data,l,j-1)
        qsort(data,j+1,h)
        
                
    else:
        pass# not doing anything
    #print(i,j)
    #print(*data)
    
        
    #print(j)
    




n=int(input())
data=list(map(int,input().split()))
qsort(data,0,n-1)
print(*data)

  

"""
10 2 16 8 12 15 6 3 9 14
           i
         j               j

step 1: choose pe
step2: if i<=j
    step i: if i smaller than PE inc i
             or
             i is bigger tahn PE stop here

    step j:  if j is bigger than PE dec j
              or
              j is smaller stop here

step3:swap i and j then again do step2

step4: swap PE and j
          
"""
