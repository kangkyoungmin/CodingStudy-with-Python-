
operation=input()

stack=[]
for o in operation:
    if o==')':
        tmp=0
        while len(stack)!=0:
            temp=stack.pop()
            if temp=='(':
                if tmp==0:
                    stack.append(2)
                else:
                    stack.append(2*tmp)
                break
            elif temp=='[':
                print(0)
                exit(0)
            else:
                tmp=tmp+int(temp) # 다른 괄호가 나오면 이전값을 더해준다
    elif o==']':
        tmp=0
        while len(stack)!=0:
            temp=stack.pop()
            if temp=='[':
                if tmp==0:
                    stack.append(3)
                else:
                    stack.append(3*tmp)
                break
            elif temp=='(':
                print(0)
                exit(0)
            else:
                tmp=tmp+int(temp)
   
    else:
        stack.append(o)
        
if not '[' in stack and not '(' in stack:
    print(sum(stack))
else:
    print(0)


