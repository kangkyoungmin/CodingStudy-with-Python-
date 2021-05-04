# 정수 4를 1,2,3의 합으로 나타내는 방법은 4가지
# 
import sys
T=int(sys.stdin.readline())

case=[]
# case들을 추가
for _ in range(T):
    case.append(int(sys.stdin.readline()))
dp=[0]*(max(case)+1)
dp[1],dp[2],dp[3]=1,2,3
# 1,2,3의 합으로 나타내기
# 
for i in range(4,max(case)+1):
    dp[i]=dp[i-1]+(dp[i-2]-dp[i-3])

    if i>=6 and i%3==0:
        dp[i]+=1

for c in case:
    print(dp[c])





