# baekjoon 2667 : 단지번호붙이기
# solved twice by JY
# DATE : 2021.04.10
# DFS 알고리즘 이용

from sys import stdin
input = stdin.readline
N = int(input())
data = [list(map(int, str(input().strip()))) for _ in range(N)]
ans = []
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
def dfs(y, x):
    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]
        if ny < 0 or ny >= N or nx < 0 or nx >= N or data[ny][nx] == 0:
            continue
        data[ny][nx] = 0
        ans[-1] += 1
        dfs(ny, nx)

for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            ans.append(1)
            data[i][j] = 0
            dfs(i, j)

print(len(ans))
ans = sorted(ans)
for i in range(len(ans)):
    print(ans[i])