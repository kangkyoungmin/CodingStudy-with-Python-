# baekjoon 13913 : 숨바꼭질 4
# solved by JY
# DATE : 2021.04.21
# BFS 알고리즘 사용
# visit[x] = x 위치에 도착하는데 걸리는 시간
# way[x] = x 위치로 오기 전 위치 값 저장

from sys import stdin
from collections import deque
input = stdin.readline
N, K = map(int, input().split())

if N == K:
    print(0, N, sep='\n')
    exit(0)

que = deque([N])
MAX = 100001
visit, way = [MAX]*MAX, [0]*MAX
visit[N], way[N] = 0, N
while que:
    x = que.popleft()
    
    if x == K:
        break

    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx < MAX and visit[nx] > visit[x]:
            visit[nx] = visit[x] + 1
            way[nx] = x
            que.append(nx)
    
print(visit[K])
ans, x = [K], K
while 1:
    x = way[x]
    ans.append(x)
    if x == N:
        break
for a in reversed(ans):
    print(a, end=' ')