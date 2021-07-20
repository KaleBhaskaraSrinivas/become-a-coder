from in_post import infix_postfix

def reverse(infix):
    rev=""
    for i in infix[::-1]:
        v=i
        if v=='(':
            v=')'
        elif v==')':
            v='('
        rev+=v
    return rev
            

infix=input()#a+b*(c-d/e)/(g-x-y)
infix_rev=reverse(infix)
prefix=infix_postfix(infix_rev)
print(prefix[::-1])

"""
(a+b)*e-c
c-e*(b+a)
1.revserse
2.infix post
3. revserse again
"""
