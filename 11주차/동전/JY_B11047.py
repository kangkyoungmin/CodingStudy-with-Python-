# baekjoon 11047 : 동전 0
# solved by JY
# DATE : 2021.03.23
# Greedy

import sys
input = sys.stdin.readline
N, K= map(int, input().split(' '))
coins = []
for _ in range(N):
    coins.append(int(input()))

answer, k = 0, K
for idx in range(N):
    if k//coins[N-idx-1] > 0 :
        answer += k//coins[N-idx-1]
        k = k%coins[N-idx-1]
    if k == 0:
        break

print(answer)