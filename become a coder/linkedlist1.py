head=None#global 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_at_end(NN):
    global head
    if head==None:
        head=NN
    else:
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=NN
def insert_at_head(NN):
    global head
    if head==None:
        head=NN
    else:
        NN.next=head
        head=NN
def insert_at_pos(NN,pos):
    global head
    if pos==1:
        insert_at_head(NN)
    elif head==None:
        head=NN
    else:
        temp=head
        p=1
        while p<pos-1:
            if temp.next==None:
                #print("List contains less count")
                break
            temp=temp.next
            p+=1
         
        #print(temp.data)
        NN.next=temp.next
        temp.next=NN          
def delete_at_end():
    global head
    if head==None:
        print("No Nodes")
    else:
        temp=head
        if head.next==None:
            head=None
            return
        while temp.next.next!=None:
            temp=temp.next
        val=temp.next.data
        temp.next=None
    return val
def delete_at_head():
    global head
    if head==None:
        print("No Nodes")
    else:
        val=head.data
        temp=head
        head=head.next
        temp.next=None
    return val
def delete_at_pos(pos):
    global head
    if head==None:
        print("No Nodes")
    elif pos==1:
        return delete_at_head()
    else:
        temp=head
        for p in range(1,pos-1):
            temp=temp.next
        val=temp.next.data
        temp.next=temp.next.next
    return val
def reverse():
    global head
    if head==None:
        print("NO Nodes")
    else:
        cur=head
        prev=None
        while cur:
            Nextnode=cur.next
            cur.next=prev
            prev=cur
            cur=Nextnode
        head=prev
            
def display(head):
    if head==None:
        print("No Nodes")
    else:
        temp=head
        while temp!=None:
            print(temp.data)
            temp=temp.next
while True:
    ch=int(input("""1.Insert at end 2.Insert at Head 3.Insert by pos 4.delete at end 5. delete at head 6. delete by pos 7.display,8.reverse the list 9.exit"""))
    if ch==1:
        data=int(input())
        NN=Node(data)# node creation
        insert_at_end(NN)
    elif ch==2:
        data=int(input())
        NN=Node(data)# node creation
        insert_at_head(NN)
    elif ch==3:
        data=int(input())
        pos=int(input())
        NN=Node(data)# node creation
        insert_at_pos(NN,pos)
    elif ch==4:
        print(delete_at_end())
    elif ch==5:
        print(delete_at_head())
    elif ch==6:
        pos=int(input())
        print(delete_at_pos(pos))    
    elif ch==7:
        display(head)
    elif ch==8:
        reverse()
        display(head)
    else:
        break
