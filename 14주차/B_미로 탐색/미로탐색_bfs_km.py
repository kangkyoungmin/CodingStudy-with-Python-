# 미로 탐색 (BFS 이용)

import sys
import copy
from collections import deque
N,M=map(int,sys.stdin.readline().split())

miro=[]
for _ in range(N):
    miro.append(list(map(int,input())))

direc_x=[1,0,0,-1] # 아래, 오른쪽, 위, 왼쪽
direc_y=[0,1,-1,0]
result=float('inf')
def bfs(a,b,cnt):
    global result
    q=deque()
    q.append([a,b,cnt])
    compare=0
    while q:
        x,y,count=q.popleft()

        if x==M-1 and y==N-1:
            compare=count
            break

        for k in range(0,4):
            dx=x+direc_x[k]
            dy=y+direc_y[k]

            if 0<=dx<M and 0<=dy<N and miro[dy][dx]==1:
                miro[dy][dx]=0
                q.append([dx,dy,count+1])
    result=min(result,compare)

bfs(0,0,1)
print(result)