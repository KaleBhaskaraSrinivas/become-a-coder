def bubblesort(n,data):
    for i in range(n-1):
        sc=0
        for j in range(n-i-1):
            if data[j]>data[j+1]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
                sc+=1
        print(data,sc)
        if sc==0:
            break
    
n=int(input())
data=list(map(int,input().split()))
bubblesort(n,data)
