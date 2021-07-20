infix=input()
n=len(infix)
out=['']*n
k=0
op={'^':4,'/':3,'*':3,'+':2,'-':2,'(':1,')':1}
st=[]
for i in range(n):
    if infix[i] not in op:
        out[k]=infix[i]
        k+=1
    else:
        if len(st)==0 or st[-1]=='(' or infix[i]=='(':
            st.append(infix[i])
        elif infix[i]==')':
            while st[-1]!='(':
                oper=st.pop()
                out[k]=oper
                k+=1
            st.pop()
                    
        else:
            while True:
                if len(st)==0 or op[infix[i]]>op[st[-1]]:
                    st.append(infix[i])
                    break
                else:
                    oper=st.pop()
                    out[k]=oper
                    k+=1
    #print(st,out)
while len(st)!=0:
    out[k]=st.pop()
    k+=1

print(''.join(out))
                    
#a+b*(c^d-e)^(f+g*h)-i  
        
    
