def postfix_infix(postfix):
    n=len(postfix)
    infix=['']*n#infix stack
    t=-1
    op=('+','-','*','/')
    for ch in postfix:
        if ch in op:
            op1=infix[t]
            infix[t]=''
            t-=1
            op2=infix[t]
            infix[t]=''
            t-=1
            ch='('+op2+ch+op1+')'
        t+=1
        infix[t]=ch
    return infix[0]
postfix=input()
infix=postfix_infix(postfix)
print(infix)

"""
abcde/-*gx-y-/+
"""
