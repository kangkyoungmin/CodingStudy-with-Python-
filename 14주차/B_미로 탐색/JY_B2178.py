# baekjoon 2178 : 미로 탐색
# solved twice by JY
# DATE : 2021.04.13
# BFS 알고리즘 사용

from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
board = [list(str(input().strip())) for _ in range(N)]
dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
INF = float('inf')
ans = [[INF] * M for _ in range(N)]
ans[0][0] = 1
que = [(0,0)]
while que:
    y, x = que.pop(0)
    if y == N-1 and x == M-1:
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        
        if board[ny][nx] == '1' and ans[ny][nx] > ans[y][x] + 1:
            ans[ny][nx] = ans[y][x] + 1
            que.append((ny,nx))

print(ans[N-1][M-1])