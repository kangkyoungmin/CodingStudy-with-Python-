# programmers L4 : 도둑질
# solved by JY
# DATE : 2021.03.11
# 

def solution(money):
    answer = 0
    dp = [[0]*(len(money) + 1) for _ in range(2)]
    dp[0][0], dp[0][1], dp[0][2] = 0, money[0], money[0]
    dp[1][0], dp[1][1], dp[1][2] = 0, 0, money[1]
    for idx in range(3, len(money)):
        dp[0][idx] = max(dp[0][idx-2] + money[idx-1], dp[0][idx-1])
    
    for idx in range(3, len(money) + 1):
        dp[1][idx] = max(dp[1][idx-2] + money[idx - 1], dp[1][idx-1])
        
    answer = max(dp[0][-2], dp[1][-1])
    
    return answer

# run test
import sys
input = sys.stdin.readline
print(solution([1, 2, 3, 1]), 4)