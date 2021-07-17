class Stack:
    def __init__(self,size):
        self.size=size
        self.data=[0]*size
        self.top=-1
    def push(self,val):
        if self.top==self.size-1:
            print("Stack overflow")
        else:
            self.top+=1
            self.data[self.top]=val
    def pop(self):
        if self.top==-1:
            return "Stack underflow"
        else:
            v=self.data[self.top]
            self.data[self.top]=0
            self.top-=1
            return v
    def display(self):
        if self.top==-1:
            print("Stack underflow")
        else:
            for i in range(self.top,-1,-1):
                print(self.data[i],end=" ")

size=int(input())
s1=Stack(size)

while True:
    ch=int(input("1. push  2.pop  3.display"))
    if ch==1:
        val=int(input())
        s1.push(val)
    elif ch==2:
        print(s1.pop())
    elif ch==3:
        s1.display()
    else:
        break
