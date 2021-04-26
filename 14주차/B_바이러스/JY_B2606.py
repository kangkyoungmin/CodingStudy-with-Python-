# baekjoon 2606 : 바이러스
# solved twice by JY
# DATE : 2021.04.13
# BFS 알고리즘 사용

from sys import stdin
from collections import defaultdict
input = stdin.readline
N, M = int(input()), int(input())
con = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    con[a].append(b)
    con[b].append(a)

ans, que = 0, [1]
check = [1] + [0]*(N-1)
while que:
    com = que.pop(0)
    for c in con[com]:
        if check[c-1] == 0:
            check[c-1] = 1
            ans += 1
            que.append(c)

print(ans)