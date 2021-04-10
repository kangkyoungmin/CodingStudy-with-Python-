# baekjoon 2294 : 동전 2
# solved by JY
# DATE : 2021.04.09
# DP 알고리즘
# dp[i] = 가치 i를 만들 수 있는 최소 동전 개수

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
value = set()
dp = [0] + [-1] * k
for _ in range(n):
    v = int(input())
    if v > k or v in value:
        continue
    value.add(v)
    for i in range(v, k + 1):
        if dp[i - v] == -1:
            continue
        if dp[i] == -1 or dp[i] > dp[i - v] + 1:
            dp[i] = dp[i - v] + 1
print(dp[k])