from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue: # 큐가 빌 때까지 반복
        x, y = queue.popleft()
        for i in range(4) : # 상하좌우 위치확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우
            if maze[nx][ny] == 0:
                continue
            # 노드를 처음 방문하는 경우에 기록 +1
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append([nx, ny])
    return maze[n-1][m-1] # 가장 오른쪽 아래까지의 최단 거리


n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))
