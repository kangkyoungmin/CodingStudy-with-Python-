# baekjoon 1303 : 전쟁 - 전투
# solved by JY
# DATE : 2021.04.13
# DFS 알고리즘 사용

from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
board = [list(str(input().rstrip())) for _ in range(M)]
visit = [[0]*(N) for _ in range(M)]
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
ans = {'W':0, 'B':0}
def dfs(y, x, st):
    global cnt
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]

        if ny < 0 or ny >= M or nx < 0 or nx >= N:
            continue
        if board[ny][nx] == st and visit[ny][nx] == 0:
            visit[ny][nx] = 1
            cnt += 1
            dfs(ny, nx, st)

for i in range(M):
    for j in range(N):
        if visit[i][j] == 1:
            continue
        visit[i][j], cnt = 1, 1
        dfs(i, j, board[i][j])
        ans[board[i][j]] += cnt*cnt
        
print(ans['W'], ans['B'], sep=' ')