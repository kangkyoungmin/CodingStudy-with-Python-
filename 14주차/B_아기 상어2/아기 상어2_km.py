# 백준 17086번

# N*M 크기의 공간
# 한 칸에는 아기 상어가 최대 1마리 존재
# 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해 지나야 하는 칸의 수
# 이동은 인접한 8방향이 가능

# 5 4
# 0 0 1 0
# 0 0 0 0
# 1 0 0 0
# 0 0 0 0
# 0 0 0 1

# 2
from collections import deque

n,m=map(int,input().split())

shark=[list(map(int,input().split())) for _ in range(n)]

direc_y=[1,0,-1,-1,-1,0,1,1]
direc_x=[-1,-1,-1,0,1,1,1,0] # 왼쪽 위부터 반시계방향

def bfs(x,y):
    q=deque()
    q.append([x,y,0])
    visited=[[True]*m for _ in range(n)]
    visited[y][x]=False
    check=False
    while q:
        ax,ay,cnt=q.popleft()
        # if shark[ay][ax]==1:
        #     break
        for j in range(0,8):
            dx=ax+direc_x[j]
            dy=ay+direc_y[j]
            if 0<=dx<m and 0<=dy<n and visited[dy][dx] and shark[dy][dx]==0:
                visited[dy][dx]=False
                q.append([dx,dy,cnt+1])
            elif 0<=dx<m and 0<=dy<n and shark[dy][dx]==1:
                count=cnt+1
                return count
count=0
result=0
for a in range(n):
    for b in range(m):
        if shark[a][b]==0:
            result=max(result,bfs(b,a))
        

print(result)

            






