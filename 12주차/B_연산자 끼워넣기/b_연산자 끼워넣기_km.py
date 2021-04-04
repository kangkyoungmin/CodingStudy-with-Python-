# 덧셈,뺄셈,곱셈,나눗셈

# 중복 체크하는 것이 중요하다

from itertools import permutations

operation=['+','-','*','//']
n=int(input())
num_list=list(map(int,input().split()))
oper_list=list(map(int,input().split()))
temp=[]
# for i,t in enumerate(oper_list):
#     for _ in range(0,t): # 개수만큼
#         temp.append(operation[i])

for i in range(4):
    tmp=[operation[i]]*oper_list[i]
    temp.extend(tmp)
    # temp.append(tmp)
# print(temp)

oper_permute=list(set(permutations(temp,len(temp))))
# print(oper_permute)
result=[0]*len(oper_permute)

for j in range(0,len(oper_permute)):
    temp2=num_list[0]
    for i in range(1,n):
        if oper_permute[j][i-1]=='+':
            temp2+=num_list[i]
        elif oper_permute[j][i-1]=='-':
            temp2-=num_list[i]
        elif oper_permute[j][i-1]=='*':
            temp2*=num_list[i]
        elif oper_permute[j][i-1]=='//':
            if temp2<0: 
                temp2=-((-temp2)//num_list[i])
            else:
                temp2//=num_list[i]
    result[j]=temp2

print(max(result))
print(min(result))
    
    
    
