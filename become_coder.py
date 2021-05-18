'''
EVEN/ODD PROGRAM

num=int(input())
if num%2==0:
    print("Even")
else:
    print("Odd")

'''        


'''
POSITIVE AND NEGATIVE NUMBERS INCLUDING WITH ZERO

num=int(input())
if num>0:
    print("+ve")
elif num<0:
    print("-ve")
else:
    print("zero")
'''


'''
13456
6 1345
5 134
4 13
3 1
1 0

num=int(input())
while num:
    r=num%10
    num=num//10
    print(r,num)
'''

'''
1 3 4 6
14
5

num=int(input())
s=0
while num:
    r=num%10
    num=num//10
    s+=r
    if num==0 and s>9:
        num=s
        print(num)
        s=0
print(s)
'''
'''
PRINTING A TABLE WITHOUT GAP

num=int(input())
for i in range(1,21):
    print(num," X ",i," = ",num*i)
'''

'''
PRINTING A TABLE WITH GAP AFTER 5'S(5x5)

num=int(input())
for i in range(1,21):
    print(num," X ",i," = ",num*i)
    if i%5==0: 
        print()
'''        

'''
PRINTING A SPACE AFTER GETTING EVEN NUM AND ODD NUM ON OUTPUT IN TABLE

num,val=map(int,input().split())
for i in range (1,21):
    print(num," X ",i," = ",num*i)
    if i%val==0:
        print()

'''
'''
PRINTING A TABLE BY SPECIFYING HOW MANY TIMES

num,r=map(int,input().split())
i=1
while i<=r:
    print(num," X ",i," = ",num*i)
    i+=1
    
'''

'''
PRINTING A TABLE BY SPECIFYING HOW MANY TIMES AND WHERE TO STOP

num,r1,r2=map(int,input().split())
if r1<=r2:
    while r1<=r2:
        print(num," X ",r1," = ",num*r1)
        r1+=1
else:
    while r2<=r1:
        print(num," X ",r2," = ",num*r2)
        r2+=1
'''
'''
SAME AS ABOVE PROGRAM IN REVERSE ORDER ALSO

num,r1,r2=map(int,input().split())
inc=1
if r1>r2:
    inc=-1
for i in range(r1,r2+inc,inc):
    print(num," X ",i," = ",num*i)

'''

'''
PRINTING A TABLE AND HOW MANY TIMES AND WHERE TO STOP AND WHICH IS DIVISIBLE BY BOTH 3 AND 5

num1,num2,r1=map(int,input().split())
for i in range(1,r1+1):
    if i%num2 and i%num1:
        print(num1,i,num1*i)

'''


'''
DIGIT COUNT OF A NUMBER

num=int(input())
dc=0
if num==0:
    dc=1
else:
    while num:
        r=num%10
        num=num//10
        dc+=1
print(dc)
'''

'''
EVEN AND ODD COUNTS OF A NUMBER

num=int(input())
ec=0
oc=0
while num:
    r=num%10
    num=num//10
    if r%2:
        oc+=1
    else:
        ec+=1
print(ec,oc)
'''

'''
EVEN ODD=(ec=2,oc=3)
EVEN =(ec=2,oc=2)
ODD=(ec=3,oc=3)
MIXED=(ec=1,oc=2)

num=int(input())
ec=0
oc=0
while num:
    r=num%10
    num=num//10
    if r%2:
        oc+=1
    else:
        ec+=1
if oc%2==1 and ec%2==0:
    print("EVEN ODD")
elif ec%2==0:
    print("EVEN")
elif oc%2:
    print("ODD")
else:
    print("MIXED")
'''

'''
PROGRAM FOR PRINTING EVEN AND ODD SEPARATELY FOR A NUMBER

num=int(input())
even=0
odd=0
ec=1
oc=1
while num:
    r=num%10
    num=num//10
    if r%2:
        odd=odd+r*oc
        oc=oc*10
    else:
        even=even+r*ec
        ec=ec*10
print(even,odd)
'''

'''
IN A NUMBER REPLACE A VALUE WITH ANOTHER VALUE

num,sv,rv=map(int,input().split())
newnum=0
c=1
while num:
    r=num%10
    num=num//10
    if r==sv:
        r=rv
    newnum=newnum+r*c
    c=c*10
print(newnum)
'''

'''
IN A NUMBER MULTIPLES OF SEARCH VALUE IS REPLACED BY REPLACE VALUE BY SPECIFYING THE REPLACE VALUES.

num,sv,rv=map(int,input().split())
rev=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
num=0
while rev:
    r=rev%10
    rev=rev//10
    if r%sv==0:
        r=rv
        rv+=1
        if rv==10:
            rv=1
    num=num*10+r
print(num)    
'''

'''
BY ABOVE CODE '0' IS NOT WORKING BY THIS BELOW CODE IS WORKING FOR '0' ALS0

num,sv,rv=map(int,input().split())
nn=0
temp=num
c=0
if rv>10:
    rv=rv%10+1
while num:
    r=num%10
    num=num//10
    c+=1
num=temp
c=c-1
while True:
    if c==-1 and num==0:
        break###
    r=num//pow(10,c)
    num=num%pow(10,c)
    c-=1
    if r%sv==0:
        r=rv
        rv+=1
        if rv==10:
            rv=1
    nn=nn*10+r
print(nn)
'''

'''
PRINTING A NUMBER BY REVERSING 1ST VALUE WITH LAST VALUE

num=int(input())
l=num%10
temp=num//10
c=0
while num:
    r=num%10
    num=num//10
    c=c+1
temp=temp*10+r
temp=temp%pow(10,c-1)
temp=l*pow(10,c-1)+temp
print(temp)
'''

'''
PROGRAM FOR A NUMBER IN THAT MIDDLE VALUES REVERSED

num=int(input())
rev=0
l=num%10
c=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
    c+=1
rev=rev%pow(10,c-1)###
rev=rev//10
rev=rev*10+1
rev=rev%pow(10,c-1)
rev=r*pow(10,c-1)+rev
print(rev)
'''


'''
FINDING A MAX AND MIN OF A NUMBER

num=int(input())
mi=num%10
ma=num%10
while num:
    r=num%10
    num=num//10
    if r>ma:
        ma=r
    if r<mi:
        mi=r
print(ma,mi)
'''

'''
FINDING MAX AND MIN VALUES OF A NUMBER AND COUNT OF HOW MANY TIMES WAS MAX AND MIN WAS THERE IN A NUMBER

num=int(input())
minimum=num%10
maximum=num%10
minc=0
maxc=0
while num:
    r=num%10
    num=num//10
    if r==minimum:
        minc+=1
    elif r<minimum:
        minimum=r
        minc=1
    if r==maximum:
        maxc+=1
    elif r>maximum:
        maximum=r
        maxc=1
print(minc,maxc)
'''

'''
FEBANOGY SERIES
IF n=10
    a b c
a b c
0 1 1 2 3 5 8 13 21 24 .....
  a b c
      a b c
c=a+b
a=b
b=c

def gen_fib(n):
    a,b=0,1
    print(a,b,end=" ")
    for i in range (3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
n=int(input())
gen_fib(n)
'''

'''
SAME AS ABOVE PROGRAM BY SPECIFYING START AND END

def gen_fib(L,U,a=0,b=1):
    if L==0:
        print(a,b,end=" ")
    if L==1:
        print(b,end=" ")
    c=0
    while c<=U:
        c=a+b
        if c>=L and c<=U:
            print(c,end=" ")
        a=b
        b=c
L,U=map(int,input().split())
gen_fib(L,U)
'''

'''
NUMBER IS FIBNOGY OR NOT WITH TEST CASES

def isfib(num):
    if num==0 or num==1:
        return True
    a=0
    b=1
    while True:
        c=a+b
        if c==num:
            return True
        if c>num:
            return False
        a=b
        b=c
T=int(input())
for i in range (T):
    num=int(input())
    print(isfib(num))

'''

'''
CLOSET FIBANOGY NUMBER FOR GIVEN NUMBER AND NUMBER IS FIBNOGY OR NOT AND TEST CASES

def isfib(num):
    if num==0 or num==1:
        return True
    a=0
    b=1
    while True:
        c=a+b
        if c==num:
            return True
        if c>num:
            print(b,num,c)
            if num-b<=c-num:
                print(b,end=" ")
            if num-b>=c-num:
                print(c)
            return False
        a=b
        b=c
T=int(input())
for i in range (T):
    num=int(input())
    print(isfib(num))

'''




















































































































            
            


































































































































































    



















































