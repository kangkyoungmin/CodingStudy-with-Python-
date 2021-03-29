# 양수, +, - 를 가지고 수를 식을 만들고 괄호를 지운다
# 괄호를 쳐서 이 식의 값을 최소로 만든다


# -를 기준으로 앞은 최소화 뒤는 최대화시킨다
temp=input().split('-')
result=0
# print(temp)

for i,t in enumerate(temp):
    if i==0:
        temp2=t.split('+')
        temp2=map(int,temp2)
        result+=sum(temp2)

    elif i!=0:
        temp2=t.split('+')
        temp2=map(int,temp2)
        temp3=-sum(temp2)
        result+=temp3

print(result)

