# n*m 게임판
# 가장 왼쪽 위 칸~ 오른쪽 아래 칸
# 반드시 오른쪽이나 아래쪽으로만 이동

# 왼쪽으로 이동은 n만큼만 가능 (비교)
# 아래쪽으로 이동은 n만큼만 가능(비교)

import sys
n=int(sys.stdin.readline())
game=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*(n) for _ in range(n)] # n*n만큼의 배열
# 가장 왼쪽 위 칸부터 오른쪽 아래 칸까지 경로의 개수
dp[0][0]=1 # 초기값 1로 할당
# dp+1씩 해주고 이들을 누적으로 더해간다
for i in range(0,n):
    for j in range(0,n):
        if i==n-1 and j==n-1:
            continue
        if i+game[i][j]<n:
            dp[i+game[i][j]][j]+=dp[i][j]
        if j+game[i][j]<n:
            dp[i][j+game[i][j]]+=dp[i][j]
print(dp[n-1][n-1])

