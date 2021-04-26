# baekjoon 12851 : 숨바꼭질 2
# solved by JY
# DATE : 2021.04.20
# BFS 알고리즘 사용

from sys import stdin
from collections import deque
input = stdin.readline
N, K = map(int, input().split())

if N >= K:
    print(N-K, 1, sep='\n')
    exit(0)

que = deque([(N, 0)])
INF = float('inf')
visit, way = [INF]*100001, 0
while que:
    x, cnt = que.popleft()
    
    if x == K:
        way += 1
        continue
    
    if visit[K] <= cnt:
        continue

    if x - 1 >= 0 and visit[x-1] > cnt:
        visit[x-1] = cnt + 1
        que.append((x-1, cnt+1))
    if x + 1 <= 100000 and x < K and visit[x+1] > cnt:
        visit[x+1] = cnt + 1
        que.append((x+1, cnt+1))
    if 2 * x <= 100000 and x < K and visit[2*x] > cnt:
        visit[2*x] = cnt + 1
        que.append((2*x, cnt+1))

print(visit[K], way, sep='\n')