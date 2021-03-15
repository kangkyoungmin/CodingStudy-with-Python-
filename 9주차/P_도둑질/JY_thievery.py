# programmers L4 : 도둑질
# solved by JY
# DATE : 2021.03.12
# DP 사용
# dp[i] = 집 i번 째까지 털었을 때 최대 금액 
# dp[0][] = 1번 집부터 털기
# dp[1][] = 2번 집부터 털기
# dp[][i] = max(dp[][i-2] + m[i-1], dp[][i-1])

def solution(money):
    dp = [[0]*(len(money) + 1) for _ in range(2)]
    dp[0][0], dp[0][1], dp[0][2] = 0, money[0], money[0]    # 1번째 집부터 털었을 경우
    for idx in range(3, len(money)):
        dp[0][idx] = max(dp[0][idx-2] + money[idx-1], dp[0][idx-1])
    
    dp[1][0], dp[1][1], dp[1][2] = 0, 0, money[1]           # 2번째 집부터 털었을 경우
    for idx in range(3, len(money) + 1):
        dp[1][idx] = max(dp[1][idx-2] + money[idx-1], dp[1][idx-1])
    
    return max(dp[0][-2], dp[1][-1])

# run test
print(solution([1, 2, 3, 1]), 4)