#퇴사2

# solutioni
# dp를 이용하여 문제를 푸는데
# dp 배열 안에 누적치의 값을 넣는다
# 
import sys
n=sys.stdin.readline()
dp=[0]*(n+1)
T=[] # day
P=[] # value
# 배열 안에 
for i in range(0,n):
    tmp1,tmp2=map(int,input().split())
    T.append(tmp1)
    P.append(tmp2)

# solution
# 상담을 할 수 있는 날에 하고 지나가는 경우와 하지 않고 넘기는 경우를
# 모두 고려한다
# value값을 더하는 경우, 

cmax=0
for j in range(0,n):
    cmax=max(cmax,dp[j]) # dp 배열 기존의 있는 값을 넣는데 0인 순간을 제외하기 위해
    # 기간이 지난 경우
    if j+T[j]>n:
        continue
    dp[j+T[j]]=max(cmax+P[j],dp[j+T[j]]) # 기존 값과 temp+value 비교

print(max(dp))







