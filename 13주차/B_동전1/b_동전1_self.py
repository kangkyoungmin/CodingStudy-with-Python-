
n,k=map(int,input().split())
coin=[int(input()) for _ in range(n)]
dp=[0]*(k+1) # 만들 수 있는 경우의 수
dp[0]=1 #초기값을 1로 설정해준다

for c in coin: # 동전을 하나씩 넣어준다
    for j in range(c,k+1): 
        dp[j]=dp[j]+dp[j-c]
print(dp[k])
 

