# baekjoon 1743 : 음식물 피하기
# solved by JY
# DATE : 2021.04.13
# DFS 알고리즘 사용

from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
input = stdin.readline
N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
for i in range(K):
    r,c = map(int, input().split())
    board[r-1][c-1] = 1

dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
ans = 0
def dfs(y, x):
    global cnt
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if board[ny][nx] == 1:
            board[ny][nx] = 0
            cnt += 1
            dfs(ny, nx)

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            board[i][j], cnt = 0, 1
            dfs(i, j)
            ans = max(ans, cnt)

print(ans)