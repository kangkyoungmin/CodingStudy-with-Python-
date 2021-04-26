# baekjoon 17086 : 아기 상어 2
# solved by JY
# DATE : 2021.04.18
# BFS 알고리즘 사용
# 모든 0에서 가까운 1의 위치를 확인 > 최댓값 갱신

from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dy = [0, 0, -1, -1, -1, 1, 1, 1]
dx = [-1, 1, -1, 0, 1, -1, 0, 1]

def bfs(y, x):
    visit = [[0]*M for _ in range(N)]
    que = [(y,x)]
    visit[y][x] = 1

    while que:
        y, x = que.pop(0)
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M or visit[ny][nx] != 0:
                continue
            if board[ny][nx] == 1:
                return visit[y][x]
            que.append((ny,nx))
            visit[ny][nx] = visit[y][x] + 1
        
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            ans = max(ans, bfs(r, c))

print(ans)