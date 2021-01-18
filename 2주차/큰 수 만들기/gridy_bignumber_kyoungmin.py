# 큰 수 만들기
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 수 중 가장 큰 숫자
# k>=1, number의 자릿수 미만
# charAt을 사용한다. 
# 배열 복사 이용하여 정렬을 이용하여 가장 큰 숫자부터 첫 번째 인덱스의 배열에 저장될 수 있도록 한다

# number="1924"
# list=[]
# for i in range(len(number)):
#     list.append(int(number[i]))
    


# def solution(number,k):
#     index=0
#     answer=[]
#     list=[]
#     temp=[]
#     if k<1 or k>len(number):
#         return False

#     for i in range(len(number)):
#         list.append(int(number[i]))

#     i=0
#     while len(list)-k>0:
#         if len(list)-k>1:
#             temp=list[index:k+1]
#             max_value=max(temp)
#         elif len(list)-k==1:
#             temp=list[index:len(list)]
#             max_value=max(temp)
#         answer.append(max_value) 
#         for j,n in enumerate(list[:k+1]):
#             if j>=index and n==max_value:
#                 index=j+1
#                 break
#         k=k+1
#     return "".join(map(str,answer))

# stack 활용() 뒤에를 k+1개만큼을 stack에 넣어주고 거기서 for문을 통하여 max값과 자른 앞부분의 stack을 비교하여 index를 구한다. 
# 인덱스 앞 부분을 삭제하고 뒷부분에 하나씩 붙인다 값을 비교하고 ... 반복한다

def solution(number,k):
    # 스택에 배열의 최초값을 집어넣어준다.
    stack=[number[0]]

    for num in number[1:]:
        # 배열 내에서 가장 큰 숫자를 STACK에 집어넣어주어야 한다,
        # 이 때 스택에 있는 값과 number배열의 데이터값과 비교하여 number가 크면 stack에서 pop하고 해당 numbber배열 값을 스택에 넣는다
        # 
        while  len(stack)>0 and num>stack[-1]and k>0:
            k-=1
            stack.pop()
        stack.append(num)

# 만약 값이 남아 있을 경우(ex. 5 4 3 2 1, k=2라면)
# 스택에는 5 4 3 2 1이 남아 있다 그러면 마지막 두 개를 짤라야 함
    if k!=0:
        stack=stack[:-k]
    return ''.join(stack)
    










# # solution("1924",2)
# print(solution("1231234",3))
# # solution("4177252841",4)

stack=[['1']]
print(stack[-1])

