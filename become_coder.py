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

'''
a   b
13  24
6   48
3   96
1   192
a//2  b*2
13*24=24+96+192

a,b=map(int,input().split())
k=0
while True:
    if a%2:
        k=k+b
    if a==0:
        break
    a=a//2
    b=b*2
print(k)

#OR
a,b=map(int,input().split())
res=0
while True:
    if a%2:
        res+=b
        break
    a=a//2
    b=b*2
print(res)
#OR
def mul(a,b,res=0):
    while a:
        if a%2:
            res+=b
        a=a//2
        b=b*2
        return res
    

a,b=map(int,input().split())
res=mul(a,b)
print(res)
'''

'''
n=6

6 3 10 5 16 8 4 2 1

n=7

7 22 11 34 17 52 26 13 40.......1

even--->//2
odd---->3*n+1

def fun(n):
    while True:
        if n%2==0:
            n//=2
            print(n,end=" ")
        else:
            n=3*n+1
            print(n,end=" ")
        if n==1:
            break
num=int(input())
fun(num)

#OR
n=int(input())
while n!=1:
    print(n,end=" ")
    if n%2:
        n=3*n+1
    else:
        n=n//2
print(n)
'''
'''
RECURSIVE METHOD FOR BELOW CODE

a   b
13  24
6   48
3   96
1   192
a//2  b*2
13*24=24+96+192

def mul(a,b):
    if a==1:
        return b
    if a%2:
        return b+mul(a//2,b*2)
    else:
        return 0++mul(a//2,b*2)
a,b=map(int,input().split())
print(mul(a,b))
'''

'''
RECURSIVE METHOD FOR FIBNOGY SERIES

def fibi(a,b,d,num):
    if d>num:
        return
    if d==1 and d<=num:
        print(a,end=" ")
        d+=1
    if d==2 and d<=num:
        print(b,end=" ")
        d+=1
    if d<=num:
        print(a+b,end=" ")
    fibi(b,a+b,d+1,num)
num=int(input())
fibi(0,1,1,num)
'''

'''    
RECURSIVE FUNCTION FOR REVERSE OF A NUMBER

re=0
def rev(num):
    global re
    if num==0:
        return re
    re=re*10+num%10
    return rev(num//10)
num=int(input())
print(rev(num))
'''
'''
ARMSTRONG NUMBER OR NOT PROGRAM

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

'''

'''
ARMSTRONG NUMBER OR NOT PROGRAM USING RECURSION METHOD

def getArm(num):
    if num==0:
        return num
    else:
        return pow ((num%10),order)+getArm(num//10)
num=int (input ("Enter a number :"))
order=len(str(num))
sum=getArm(num)
if sum==int(num):
    print(num,"is an Armstrong Number.")
else:
    print(num,"is not an Armstrong Number.")

#OR
def digitcount(num):
    dc=0
    while num:
        num=num//10
        dc+=1
    return dc
def isarmstrong(num):
    if num==0:
        return 0
    return pow(num%10,dc)+isarmstrong(num//10)
num=int(input())
dc=digitcount(num)
print(num==isarmstrong(num))

'''

'''
RECURSIVE  METHOD FOR PERFECT NUMBER

import math as m
def isperfect(num):
    res=1
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            res+=i+num//i
    return res==num
num=int(input())
print(isperfect(num))
'''
'''
LCM USING RECURSION METHOD
def lcm(a,b):
    lcm.multiple=lcm.multiple+b
    if((lcm.multiple % a == 0) and (lcm.multiple % b == 0)):
        return lcm.multiple;
    else:
        lcm(a, b)
    return lcm.multiple
lcm.multiple=0
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if(a>b):
    LCM=lcm(b,a)
else:
    LCM=lcm(a,b)
print(LCM)

'''
'''
HCF OR GCD USING RECURSION METHOD
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b, a%b) 
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
print('HCF or GCD of %d and %d is %d' %(first, second, hcf(first, second)))
'''
'''
EUCLIDIANS ALGORITHM FOR  HCF OR GCD
def gcd(a, b):
    if a == 0 :
        return b
     
    return gcd(b%a, a)
 
a = int(input())
b = int(input())
print("gcd(", a , "," , b, ") = ", gcd(a, b))
 
'''

'''
PRONIC NUMBER
42=6*7

from math import *

def ispronic(num):
    a=int(sqrt(num))
    return a*(a+1)==num
num=int(input())
print(ispronic(num))
'''

'''
DISARIUM NUMBER
175=1^1+7^2+5^3=175

def isdisarium(num):
    dc=0
    temp=num
    while(temp):
        temp=temp//10
        dc+=1
    temp=num
    res=0
    while temp:
        r=temp%10
        temp=temp//10
        res=res+pow(r,dc)
        dc-=1
    return res==num
num=int(input())
print(isdisarium(num))

'''

'''
HARSHAD NUMBER
18=1+8=9 and 18 is divisible by 9


def isharshad( num ) :
    sum = 0
    temp = num
    while temp > 0 :
        sum = sum + temp % 10
        temp = temp // 10
    return num % sum == 0
num=int(input())
print(isharshad(num))
'''

'''
ADDING TWO DIGITS PROGRAM IN LEETCODE
38=3+8=11=1+1=2

class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while num:
            r=num%10
            num//=10
            s+=r
            if num==0 and s>9:
                num=s
                s=0
        return s
'''

'''
COMPLEMENT OF BASE 10 INTEGER
5=101
5 COMPLEMENT=010=2_

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=0
        t=0
        if n==0:
            return 1
        while n:
            r=n%2
            n=n//2
            if r==0:
                s=s+(2**t)
            t=t+1
        return s
'''

'''
ARRANGING COINS PROBLEM IN LEETCODE

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 0:
            raise ValueError('the input is invalid')
        if n == 0:
            return 0

        counter = 0
        row = 1
        while n - row >= 0:
            n -= row
            counter += 1
            row += 1

        return counter
'''

'''
BINARY NNUMBER WITH ALTERNATING BITS IN LEETCODE PROGRAM

5=101
TRUE

7=111
FALSE

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        d=n%2
        n=n//2
        while n:
            r=n%2
            n=n//2
            if(r==d):
                return False
            d=r
        return True
'''

'''
POWER OF FOUR PROGRAM IN LEETCODE


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p=0
        while 4**p<n:
            p+=1
        return 4**p==n


'''

'''

NUMBER OF 1 BITS PROGRAM IN LEETCODE

class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        print(n)
        one_count = 0
        for i in n:
            if i == "1":
                one_count+=1
        return one_count

'''


'''
PRIME NUMBER OF SET BITS IN BINARY REPRESENTATION IN LEETCODE PROGRAM

Input: left = 6, right = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def popcount(i):
            return bin(i)[2:].count('1')
        count = 0
        for j in range(left,right+1):
            if popcount(j) in [2,3,5,7,11,13,17,19]:
                 count +=1
        return count
#OR
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(num):
            if num==1:
                return False
            s=int(math.sqrt(num))
            for i in range(2,s+1):
                if num%i==0:
                    return 0
            return 1
        rc=0
        for n in range(left,right+1):
            sbc=0
            while n:
                r=n%2
                n=n//2
                sbc+=r
            rc+=isprime(sbc)
        return rc
'''

'''
HAPPY NUMBER IN LEETCODE PROGRAM

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

n=19
TRUE
1^2+9^2=82
8^2+2^2=68
6^2+8^2=100
1^2+0^2+0^2=1

class Solution:
    def isHappy(self, n: int) -> bool:
        return self.solve(n,{})
    def solve(self,n,visited):
        if n == 1:
            return True
        if n in visited:
             return False
        visited[n]= 1
        n = str(n)
        l = list(n)
        l = list(map(int,l))
        temp = 0
        for i in l:
            temp += (i**2)
        return self.solve(temp,visited)
       
#OR

class Solution:
    def isHappy(self, n: int) -> bool:
        res=0
        while n:
            r=n%10
            n=n//10
            res+=pow(r,2)
            if n==0 and (res>=10 or res==7):
                print(res,end=" ")
                n=res
                res=0
        return res==1
'''

'''
Subtract the Product and Sum of Digits of an Integer leetcode problem


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,p=0,1
        while n:
            r=n%10
            n=n//10
            s=s+r
            p=p*r
        return p-s

'''

'''        
Maximum 69 Number leetcode problem

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
'''

'''
num=5
*****
*****
*****
*****
*****

num = int(input())
for i in range(num):
        for j in range(num):
                print("*",end = "")
        print()

'''

'''
num=5
12345
12345
12345
12345
12345

num = int(input())
for i in range(num):
        for j in range(num):
                print(j+1,end = "")
        print()
'''

'''
num=5
11111
22222
33333
44444
55555

num = int(input())
for i in range(num):
        for j in range(num):
                print(i+1,end = "")
        print()

'''

'''
num=5
54321
54321
54321
54321
54321

num = int(input())
for i in range(1,num+1):
        for j in range(num,0,-1):
                print(j,end = "")
        print()

'''

'''
num=5
12345
54321
12345
54321
12345

num=int(input())
for i in range(num):
        if i%2==0:
                for j in range(1,num+1):
                        print(j,end="")
        else:
                for j in range(num,0,-1):
                        print(j,end="")
        print()        
                
'''

'''
num=5

11111
12345
33333
12345
55555

num=int(input())
for i in range(num):
        if i%2==0:
                for j in range(1,num+1):
                        print(j,end="")
        else:
                for j in range(1,num+1):
                        print(i,end="")
        print()        

'''

'''
num=5
12345
22345
32345
42345
52345

num =int(input())
for i in range(1,num+1):
        for j in range(1,num+1):
                if j==1:
                        print(i,end="")
                else:
                        print(j,end = "")
        print()

'''

'''
num=5
54321
22222
54321
44444
54321

num=int(input())
for i in range(1,num+1):
        for j in range(1,num+1):
                if i%2:
                        print(num+1-j,end="")
                else:
                        print(i,end="")
        print()

'''

'''
num=5
10101
10101
10101
10101
10101

num=int(input())
for i in range(1,num+1):
        for j in range(1,num+1):
                if j%2==0:
                        print(0,end="")
                else:
                         print(1,end="")
        print()
'''

'''
num=5
10101
01010
10101
01010
10101

num=int(input())
t=0
for i in range(1,num+1):
        for j in range(1,num+1):
                if t==0:
                        t=1
                        print(t,end="")
                else:
                        t=0
                        print(t,end="")
        print()


'''


'''
num=5
*
**
***
****
*****

num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
'''

'''
num=5
*****
****
***
**
*

num=int(input())
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
'''

'''
num=5
1
22
333
4444
55555

num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

'''

'''
num=5
55555
4444
333
22
1

num=int(input())
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()
'''

'''
num=5
1
12
123
1234
12345

num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''

'''
num=5
54321
4321
321
21
1


num=int(input())
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
'''

'''
num=5
12345
1234
123
12
1

num=int(input())
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''

'''
num=5
12345
4321
123
21
1

num=int(input())
for i in range(num,0,-1):
    if i%2==0:
        for j in range(i,0,-1):
            print(j,end="")
    else:
         for j in range(1,i+1):
             print(j,end="")
    print()
        
'''

'''
num=5
1
01
101
0101
10101

num=int(input())
for i in range(1,num+1):
    for j in range(i,0,-1):
        if j%2==0:
            print("0",end="")
        else:
             print("1",end="")
    print()
'''

'''
num=5
1
22
323
4234
52345

num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        if j==1:
            print(i,end="")
        else:
             print(j,end="")
    print()
'''

'''
num=5
    *
   **
  ***
 ****
*****


num=int(input())
for i in range(1,num+1):
    for s in range(num,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
             print("*",end=" ")
    print()

'''

'''
*****
 ****
  ***
   **
    *

num=int(input())
for i in range(num):
    for j in range(i):
        print(" ",end=" ")
    for j in range(num-i):
             print("*",end=" ")
    print()
'''

'''
num=5
        *
      * * *
    * * * * *
   * * * * * * * 
 * * * * * * * * *


num=int(input())
for i in range(1,num+1):
    for s in range(1,num-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()

'''

'''
USING LIST
NUM=5
100
200
300
400
500

n=int(input())
data = [None for i in range(n)]
for i in range(n):
    val = int(input())
    data[i] = val
print(data)
'''

'''
USING LIST
NUM=5
100 200 300 400 500

n=int(input())
data = list(map(int,input().split()))
print(data)
'''

'''
INDEX BASED LIST

n=int(input())
data = list(map(int,input().split()))
for i in range(n):
    print(data[i],end=" ")
'''

'''
VALUE BASED LIST PROGRAM

n=int(input())
data = list(map(int,input().split()))
for i in range(n):
    print(i,end=" ")
'''

'''
TOTAL SUM OF LIST USING FUNCTIONS

def total_marks(n,data):
    res=0
    for i in data:
        res+=i
    return res
n=int(input())
data = list(map(int,input().split()))
total = total_marks(n,data)
print(total)
'''

'''
COUNTING EVEN AND ODD NUMBERS IN A LIST

def total_marks(n,data):
    ec=0
    oc=0
    for i in range(n):
        if data[i]%2:
            oc+=1
        else:
            ec+=1
    return(ec,oc)
n=int(input())
data = list(map(int,input().split()))
total = total_marks(n,data)
print(*total)
'''
'''
PRIME NUMBER COUNT PROGRAM USING LIST
NUM=5
3 7 9 11 13
4


import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
            

def countPrimes(n,data):
    pc=0
    for i in data:
        if isprime(i):
            pc+=1
    return pc
    
n=int(input())
data = list(map(int,input().split()))
pc=countPrimes(n,data)
print(pc)
'''

'''
FIND PRIME NUMBERS AND NON PRIME NUMBERS PROGRAM USING LIST
NUM=5
3 7 9 11 13

3 7 11 13

import math as m
def isprime(num):
    if num==1:
        return 0
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1

def findPrimes(n,data):
    prime=[]
    nonprimes=[]
    for i in data:
        if isprime(i):
            prime.append(i)
        else:
            nonprimes.append(i)
    return prime,nonprimes
    
  
    
n=int(input())
data = list(map(int,input().split()))
primes,np=findPrimes(n,data)
print(*primes)
print(*np)
'''


'''
SUM OF PRIME NUMBERS IN LIST OF EVERY ELEMENT USING FUNCTIONS

def res(n):
    s=0
    while n:
        r=n%10
        n=n//10
        s+=r
    return s
def sumofdigits(n,data):
    for i in range(n):
        data[i]=res(data[i])

n=int(input())
data = list(map(int,input().split()))
sumofdigits(n,data)
print(*data)

'''

'''
REVERSE OF A NUMBER IN A LIST USING FUNCTIONS

from math import *
def rev(n):
    k=0
    while n:
        r=n%10
        n=n//10
        k=k*10+r
    return k
def revofdigits(n,data):
    for i in range(len(data)):
        data[i] = rev(data[i])
        
n=int(input())
data = list(map(int,input().split()))
revofdigits(n,data)
print(*data)
'''

'''
PALINDROME OF A NUMBER USING LIST BY FUNCTIONS


def palindromeCount(n,arr):
    pali=0
    for i in range(n):
        temp,num=0,arr[i]
        while arr[i]:
            r=arr[i]%10
            arr[i]//=10
            temp = temp*10+r
        if temp==num:
            pali+=1
    return pali

n=int(input())
arr = list(map(int,input().split()))
print(palindromeCount(n,arr))
'''

'''
FINDING MIN AND MAX OF A LIST USING FUNCTIONS

n=6

45 32 431 171 184 13

13 431

def min_max(n,data):
    s,l=data[0],data[0]
    for i in data:
        if s>i:
            s=i
        if l<i:
            l=i
    return s,l
n=int(input())
data = list(map(int,input().split()))
mi,ma=min_max(n,data)
print(mi,ma)

'''

'''
FIND MIN OF A LIST AND POSITION AND COUNT

def findmin(n,data):
    s,c=data[0],0
    ind=[]
    for i in data:
        if s==i:
            c+=1
        if s>i:
            s=i
            c=1
    ind=[s,c]
    for i in range(n):
        if s==data[i]:
            ind.append(i)
    return ind

n=int(input())
data = list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)
'''

'''
SUPER MIN
5
12 34 65 57 45
21

SUPER MAX
5
12 20 45 56 32
65

SUPERMIN AND SUPERMAX
5
12 23 56 44 32
21 65



def maxnumber(n,data):
    max=data[0]
    for i in range(n):
        if max<data[i]:
            max=data[i]
    return max
def minnumber(n,data):
    min=data[0]
    for i in range(n):
        if min>data[i]:
            min=data[i]
    return min
def min_max_rev(num):
    rev1=0
    while num:
        r=num%10
        num//=10
        rev1=rev1*10+r
    return rev1


n=int(input())
data = list(map(int,input().split()))

max=maxnumber(n,data)
maxrev=min_max_rev(max)
min=minnumber(n,data)
minrev=min_max_rev(min)


for i in range(n):
    if data[i]==max:
        data[i]=maxrev
    if data[i]==min:
        data[i]=minrev
supermax=maxnumber(n,data)
supermin=minnumber(n,data)

if supermax==maxrev:
    print("super max")
else:
    print("not super max")
if supermin==minrev:
    print("super min")
else:
    print("not super min")

'''

'''
ORIGINAL VALUES
10
4 3 1 5 2 6 3 2 6 7

OUTPUT:

4 3 1 5 2 6 7

def original(n,data):
    b=[]
    for i in data:
        if i not in b:
            b.append(i)
    return b

n=int(input())
data = list(map(int,input().split()))
d=original(n,data)
print(*d)
'''

'''
ELEMENT COUNT IN A LIST BY FUNCTIONS

def match_count(n,data):
    for i in data:
        if i not in orig:
            orig.append(i)
    c=0
    for i in range(len(orig)):
        if orig[i]==data[i]:
            c+=1
    return orig,c
n=int(input())
orig=[]
data=list(map(int,input().split()))
print(match_count(n,data))
'''

'''
SORTING THE ELEMENTS INA LIST BY USING FUNCTIONS AND IF SAME PLACE THRER MEANS INCREMENTTING AND PRINTING COUNT

def sort_match(n,data):
    for i in data:
        if i not in orig:
            orig.append(i)
    orig.sort()
    c=0
    for i in range(len(orig)):
        if orig[i]==data[i]:
            c+=1
    return orig,c
n=int(input())
orig=[]
data=list(map(int,input().split()))
print(sort_match(n,data))

'''
'''
HOW MANY DIFFERENT TYPES OF ELEMENTS AND HOW MANY TIMES IT IS REPEATING

n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
for k in dic.keys():
    print(k,dic[k])
'''
'''
PRINTING MAXIMUM ELEMENT IN A DICTIONARY

n=int(input())
data=list(map(int,input().split()))
dic={}
m=0
for i in data:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
    if m<dic[i]:
        m=dic[i]
for k in dic.keys():
    if dic[k]==m:
        print(k,dic[k])
'''

'''
PRINTING SECOND INDEX VALUES IF THERE IS NO SECOND INDEX RETURN FALSE USING LIST

def search(n,data,s):
    c=0
    if data.count(s)<2:
        return False
    for i in range(n):
        if data[i]==s:
            c+=1
        if c==2:
            return i

n=int(input())
data=list(map(int,input().split()))
s=int(input())
print(search(n,data,s))
'''

'''
PRINTING SECONG LARGEST NUMBER IN LIST AND SET

n=int(input())
data=list(map(int,input().split()))
data.sort()
k=set(data)
k=list(k)
print(k[-2])

#OR

def secondlargest(n,data):
    sh,fh=data[0],data[0]
    for i in data[1:]:
        if i>fh:
            sh=fh
            fh=i
        if i>sh and i<fh:
            sh=i
    return sh
n=int(input())
data=list(map(int,input().split()))
print(secondlargest(n,data))
'''


'''
SORTED OR NOT USING LIST

n=int(input())
data=list(map(int,input().split()))
s=data.copy()
k=data.copy()
s.sort()
k.sort()
k.reverse()
if s==data or k==data:
    print("sorted")
else:
    print("not sorted")

#OR

def issorted(n,data):
    if(data==sorted(data) or data==list(reversed(sorted(data)))):
        return True
    return False
n=int(input())
data=list(map(int,input().split()))
print(issorted(n,data))
'''        

'''
BOUNCY NUMBER LIST USING FUNCTIONS

1 2 1 2 1
TRUE


def isbouncy(n,data):
    if data[0]<data[1]:
        h=True
        l=False
    else:
        l=True
        h=False
    for i in range(1,n-1):
        if (h==True and data[i]<=data[i+1]) or (l==True and data[i]>=data[i+1]):
            return False
        h=not h
        l=not l
    return True

n=int(input())
data=list(map(int,input().split()))
print(isbouncy(n,data))
'''
           
'''
MAXIMUM SORTING OF ELEMENTS IN ASCENDING ORDER


def maxsort(n,data):
    f=s=0
    for i in range(n-1):
        if data[i]<data[i+1]:
            f=f+1
        else:
            if f+1>s:
                s=f+1
            f=0
    if f+1>s:
        return f+1
    return s
n=int(input())
data=list(map(int,input().split()))
q=maxsort(n,data)
print(q)
'''


'''
SORTING MAX ONES

def max_ones(n,arr):
    temp,count=0,0
    for i in arr:
        if i==1:
            temp+=1
        else:
            if count<temp:
                count=temp
            temp=0
    return max(temp,count)
n=int(input())
arr=list(map(int,input().split()))
print(max_ones(n,arr))
'''


'''
MOVING ZEROS TO END OF A LIST


def movezeros(n,arr):
    for i in arr:
        if i==0:
            arr.insert(n,0)
            arr.remove(0)

n=int(input())
data = list(map(int,input().split()))
movezeros(n,data)
print(*data)
'''


'''
LEFT ROTATE A LIST BY D POSITIONS

6
1 2 3 4 5 6
4
5 6 1 2 3 4

6
1 2 3 4 5 6
2
3 4 5 6 1 2

def reverse(arr,l,h):
    while(l<h):
        arr[l],arr[h]=arr[h],arr[l]
        l+=1
        h-=1

def rotateList(n,arr,r):
    r=r%n
    reverse(arr,0,r-1)
    reverse(arr,r,n-1)
    reverse(arr,0,n-1)

n=int(input())
arr = list(map(int,input().split()))
r=int(input())
rotateList(n,arr,r)
print(*arr)
'''

'''
LEADERS OF THE LIST

6
10 19 23 29 3 7

29 7


n=int(input())
data=list(map(int,input().split()))
def leaders(n,data):
    for i in range(n):
        if data[i]==max(data[i:]):
            print(data[i],end=" ")
    print()
leaders(n,data)

'''

'''
SUM OF I-D ARRAY LEET CODE PROBLEM

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(1,n):
            nums[i]=nums[i]+nums[i-1]
        return nums

'''

'''
NUMBER OF GOOD PAIRS LEET CODE PROBLEM

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        c=0
        for i in dic.values():
            c+=i*(i-1)//2
        return c
'''

'''
XOR OPERATION IN AN ARRAY LEET CODE PROBLEM

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i=1
        res=start
        start=2+start
        while(i<n):
            res=res^start
            start=2+start
            i=i+1
        return res
'''

'''
FIND THE HIGHEST ALTITUDE USING LEET CODE PROBLEM

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[]
        ans.append(0)
        for i in range(0,len(gain)):
            tmp=ans[i]+gain[i]
            ans.append(tmp)
            
        return max(ans)
'''

'''
FIND THE NUMBERS WITH EVEN NUMBER OF DIGITS LEET CODE PROBLEM

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count
'''


'''
SQUARES OF SORTED ARRAY LEET CODE PROBLEM

inpu=[-4,-1,0,5,6]
output=[0,1,16,25,36]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        square_elements = []
        for item in nums:
            prod = item*item
            square_elements.append(prod)
        square_elements.sort()
        return square_elements
'''

'''
MAXIMUM PRODUCT OF TWO ELEMENTS IN ARRAY LEET CODE PROBLEM

nums=[3,4,5,2]
out=12(3*4)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=len(nums)
        nums=sorted(nums,reverse=True)
        return (nums[0]-1)*(nums[1]-1)
'''

'''
Number of Students Doing Homework at a Given Time lLEET CODE PROBLEM

Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
        
'''

'''
Average Salary Excluding the Minimum and Maximum Salary LEETCODE PROBLEM
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return (sum(salary)/len(salary))
'''

'''
SORT ARRAY BY PARITY LEETCODE PROBLEM

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = deque()
        for i in nums:
            if i%2:
                arr.append(i) LEETCODE PROBLEM
            else:
                arr.appendleft(i)
        return arr
'''

'''
Sum of Unique Elements

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        
        for num in nums:
            if nums.count(num) == 1:
                result += num
        
        return resulT

'''

'''
Maximum Number of Balls in a Box LEETCODE PROBLEM

Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
 

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dict={}
        for i in range(lowLimit, highLimit+1):
            total=0
            for j in str(i):
                total += int(j)
            if(total not in dict):
                 dict[total] = 0
            dict[total] += 1
        return max([dict[i] for i in dict])
'''

'''
Height Checker LEETCODE PROBLEM

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
'''

'''
Move Zeroes LEETCODE PROBLEM

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1

        while i < len(nums):
            nums[i] = 0
            i += 1
'''

'''
Make Two Arrays Equal by Reversing Sub-arrays LEETCODE PROBLEM

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in arr:
            if i in target:
                target.remove(i)
        if len(target)>0:
            return False
        else:
            return True
'''











