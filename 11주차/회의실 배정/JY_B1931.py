# baekjoon 1931 : 회의실 배정
# solved twice by JY
# DATE : 2021.03.26
# Greedy 알고리즘

import sys
input = sys.stdin.readline
N = int(input())
conf = [list(map(int, input().split())) for _ in range(N)]
conf = sorted(conf, key=lambda x:(x[1], x[0]))
ans, pre = 1, conf[0]
for idx in range(1, N):
    if pre[1] <= conf[idx][0]:
        pre = conf[idx]
        ans += 1
print(ans)
