def infix_postfix(infix):
    n=len(infix)
    pf=['']*n
    x=0
    st=['']*n
    t=-1
    op={'^':4,'/':3,'*':3,'+':2,'-':2,'(':5,')':5}
    for ch in infix:
        if ch not in op:
            pf[x]=ch
            x+=1
        elif ch==')':
            while st[t]!='(':
                oper=st[t]
                st[t]=''
                t-=1
                pf[x]=oper
                x+=1
            st[t]=''
            t-=1


        else:
            while True:
                if t==-1 or st[t]=='(':
                    t+=1
                    st[t]=ch
                    break
                elif op[ch]>op[st[t]]:
                    t+=1
                    st[t]=ch
                    break
                elif op[ch]<=op[st[t]]:
                    oper=st[t]
                    st[t]=''
                    t-=1
                    pf[x]=oper
                    x+=1

    while t!=-1:
        oper=st[t]
        st[t]=''
        t-=1
        pf[x]=oper
        x+=1
    return ''.join(pf)

infix=input()
postfix=infix_postfix(infix)
print(postfix)
        
            

                 
                    
                    
                    
