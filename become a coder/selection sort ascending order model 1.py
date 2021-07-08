def maxi(data,n):
    mi=0
    me=data[0]
    for i in range(1,n):
        if me<data[i]:
            me=data[i]
            mi=i
    return mi

def selectionsort(n,data):
    j=n-1
    for i in range(n-1):
        mi=maxi(data,n-i)
        data[mi],data[j]=data[j],data[mi]
        j-=1
        print(data)



n=int(input())
data=list(map(int,input().split()))
selectionsort(n,data)
    
