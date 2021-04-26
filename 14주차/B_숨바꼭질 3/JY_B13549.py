# baekjoon 13549 : 숨바꼭질 3
# solved by JY
# DATE : 2021.04.21
# BFS 알고리즘 사용
# visit[x] : x 위치에 도착하는데 걸리는 시간

from sys import stdin
from collections import deque
input = stdin.readline
N, K = map(int, input().split())
if K <= N:
    print(N-K)
    exit(0)

que = deque([N])
MAX = 100001
visit = [MAX]*MAX
visit[N] = 0

while que:
    x = que.popleft()
    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx < MAX and visit[nx] > visit[x] + 1:
            visit[nx] = visit[x]
            if nx != 2*x:
                visit[nx] += 1
            que.append(nx)
    
print(visit[K])