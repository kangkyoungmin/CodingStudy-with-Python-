# 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에 길거리에서 찾은 수에 포함된 숫자들을 섞어
#30의 배수가 되는 가장 큰 수를 만들고 싶어한다

# 마르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라

# 문자열을 하나 하나 쪼개어 입력받고

# from itertools import permutations
# n=int(input())

# m=str(n)
# a=list(permutations(m,len(m)))
# print(a)
# temp=""
# result=0
# a.sort()
# for d in a:
#     temp=max("".join(d),temp)
#     if int(temp)%30==0:
#         result=temp
#     else:
#         result=-1
#     temp="".join(d)
# # for i in str(n):
# #     permutations()
# #     m.append(i)

# # m.sort()
# print(result)
# # for j in m

N=input()
N=sorted(N,reverse=True)
sum=0
if '0' not in N:
    print(-1)

else:
    for i in N:
        sum+=int(i)
    if sum%3!=0:
        print(-1)
    else:
        print("".join(N))
