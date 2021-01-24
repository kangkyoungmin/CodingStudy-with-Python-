# baekjoon 2178 : 미로 탐색
# solved by JY
# DATE : 2020.01.19
# BFS

import collections
import sys

def BFS():
    deq = collections.deque()
    deq.append([0, 0])
    visit[0][0] = 1

    while len(deq) > 0:
        y, x = deq.popleft()    # 선입선출
        for i in range(4):      # 상하좌우 확인
            yy, xx = y + dy[i], x + dx[i]
            if yy >= 0 and yy < N and xx >= 0 and xx < M:
                # 지금 가는 곳이 1이란 조건 하에 내가 가면 더 최단경로라면 deq에 추가
                if (visit[y][x] + 1 < visit[yy][xx] or visit[yy][xx] == 0) and miro[yy][xx] != 0: 
                    deq.append([yy, xx])
                    visit[yy][xx] = visit[y][x] + 1

    print(visit[N-1][M-1])

# run test
N, M = map(int, sys.stdin.readline().split())
miro, visit = [[0]*M for _ in range(N)], [[0]*M for _ in range(N)]
for i in range(N):
    miro[i] = list(map(int, sys.stdin.readline().rstrip()))
    
dy = [-1, 1, 0, 0]  # 상하좌우
dx = [0, 0, -1, 1]

BFS()