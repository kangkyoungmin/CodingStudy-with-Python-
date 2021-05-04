# 1학년 5567번
import sys
N=int(sys.stdin.readline())
equation=list(map(int,sys.stdin.readline().split()))
dp=[[0] *21 for _ in range(N+1)]
dp[0][equation[0]]=1

for i in range(1,N-1):
    tmp=equation[i]
    for j in range(0,21):
        if dp[i-1][j]>0:
            if 0<=tmp+j<=20:
                # dp[i][j+tmp]=max(dp[i][j+tmp]+1,dp[i-1][j+tmp]+1)
                dp[i][j+tmp]+=dp[i-1][j]
            if 0<=j-tmp<=20:
                # dp[i][j-tmp]=max(dp[i][j-tmp]+1,dp[i-1][j-tmp]+1)
                dp[i][j-tmp]+=dp[i-1][j]

print(dp[N-2][equation[N-1]])
    

# +또는 -만을 사용해서 만든다
