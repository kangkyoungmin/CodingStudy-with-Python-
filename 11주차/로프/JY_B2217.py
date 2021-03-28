# baekjoon 2217 : 로프
# solved by JY
# DATE : 2021.03.24
# Greedy

import sys
input = sys.stdin.readline
N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope = sorted(rope,reverse=True)
ans = 0
for idx in range(N):
    ans = max(ans, (idx+1)*rope[idx])
print(ans)