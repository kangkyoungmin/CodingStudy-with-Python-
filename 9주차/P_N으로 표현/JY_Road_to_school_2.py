# programmers L3 : 등굣길
# solved by JY + best
# DATE : 2021.03.11
# DP 사용
# dp[y][x] = (x,y)까지의 최단경로의 개수
# 오른쪽과 아래쪽만 이동 가능 > puddles만 아니면 무조건 최단경로임
# 왼쪽과 위쪽의 dp 값을 더하면 해당 위치의 최단경로 개수

def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for x, y in puddles:
        dp[y][x] = -1
    dp[1][1] = 1
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if y == x == 1:
                continue
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            else:
                dp[y][x] = (dp[y][x-1] + dp[y-1][x])%1000000007
    
    return dp[n][m]

# run test
print(solution(4, 3, [[2,2]]), 4)