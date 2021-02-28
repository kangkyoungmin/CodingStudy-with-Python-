# 회사에 있는 사람
# 각 직원은 자기가 원할 때 출근하고 아무때나 퇴근할 수 있다
# 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있고, 어떤 사람이 회사에 들어왔는지 나갔는지가 기록되어 있음
# 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오

# 회사에는 동명이인 x, 대소문자가 다른 경우 다른 이름이다
# 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열

# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 출력

n=int(input())
input_list=[]
result=[]
for i in range(n):
    input_list.append(list(input().split()))

for temp in input_list:
    if temp[1]=='enter':
        result.append(temp[0])
    else:
        result.remove(temp[0])
result.sort(reverse=True)
for r in result:
    print(r)

# for e,i in zip(input_list,range(len(input_list))):
#     status[e[1]].append([e[0],i])
# print(status)

# status['enter'].sort(reverse=True)

# for enter in status['enter']:
#     check=True
#     for leave in status['leave']:
#         if enter==leave:
#             check=False
#             status['leave'].remove(leave)
#     if check==True:
#         print(enter)

            
    



