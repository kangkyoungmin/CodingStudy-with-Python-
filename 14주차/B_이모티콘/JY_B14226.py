# baekjoon 14226 : 이모티콘
# solved by JY
# DATE : 2021.04.23
# check[e][c] : 화면 e개, 클립보드 c개 인 경우를 수행했다면 True

from sys import stdin
from collections import deque
input = stdin.readline
S = int(input())
MAX = 1001
check = [[False]*MAX for _ in range(MAX)]
check[1][0] = True
que = deque([[1, 0, 0]])

while que:
    e, c, cnt = que.popleft()
    if e == S:
        break

    if e != c and not check[e][e]:
        check[e][e] = True
        que.append([e,e,cnt+1])

    for n_e in [e + c, e-1]:
        if 0 < n_e < MAX and not check[n_e][c]:
            check[n_e][c] = True
            que.append([n_e,c,cnt+1])

print(cnt)