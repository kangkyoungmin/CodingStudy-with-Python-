# baekjoon 2293 : 동전 1
# solved by JY + ans
# DATE : 2021.04.08
# DP 알고리즘 사용
# dp[i] = 가치 i를 만들 수 있는 경우의 수
# dp[i] += dp[i-v]의 경우들에 v를 붙인 경우

import sys
input = sys.stdin.readline
n, k = map(int, input().split())

dp = [1] + [0] * k
for _ in range(n):
    v = int(input())
    for i in range(v, k + 1):
        if i - v >= 0:
            dp[i] += dp[i - v]
print(dp[k])