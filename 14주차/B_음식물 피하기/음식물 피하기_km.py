# 백준 1743번
# 뭉치게 된다? 즉 bfs를 써라
# 세로길이, 가로길이, 음식물 쓰레기의 개수가 주어진다
# K개의 음식물이 떨어진 좌표 (r,c)가 주어진다

# r은 위에서부터, c는 왼쪽에서부터가 기준
# 첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력

from collections import deque
N,M,K=map(int,input().split()) # 세로, 가로, 음식물 쓰레기의 개수

garbage=[[0]*M for _ in range(N)]
for i in range(0,K):
    a,b=map(int,input().split()) # a: 세로 b: 가로
    garbage[a-1][b-1]=1

direc_x=[1,0,-1,0] # 오른쪽,아래,왼쪽,위
direc_y=[0,1,0,-1]
result=0
def bfs(a,b):
    global result
    q=deque()
    q.append([b,a])
    garbage[a][b]=0
    count=1

    while q:
        x,y=q.popleft() # 가로,세로

        for i in range(0,4):
            dx=x+direc_x[i]
            dy=y+direc_y[i]

            if 0<=dx<M and 0<=dy<N and garbage[dy][dx]==1:
                garbage[dy][dx]=0
                q.append([dx,dy])
                count+=1
    result=max(result,count)

for c in range(0,N):
    for d in range(0,M):
        if garbage[c][d]==1: # c: 세로 # d: 가로
            bfs(c,d)

print(result)


