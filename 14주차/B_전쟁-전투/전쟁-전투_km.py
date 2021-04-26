# 우리 병사와 적국 병사가 섞여 싸우게 되었다
# 하얀 옷을 입고, 적국의 병사들은 파란옷을 입음
# 같은 팀의 병사들은 모이면 모일수록 강해짐
# N명이 뭉쳐있을 때 N^2의 위력을 낸다
# 대각으로만 인접한 경우 뭉쳐있다고 보지 않는다

# 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력

from collections import deque
N,M=map(int,input().split())

war=[]
for _ in range(0,M):
    war.append(list(input()))
# print(war)

result=[0,0]
direc_x=[0,0,1,-1] # 왼쪽,오른쪽,위,아래
direc_y=[-1,1,0,0]
visited=[[0]*N for _ in range(M)] #  방문 배열
def bfs(a,b,char):
    if a<0 or b<0 or a>M-1 or b>N-1:
        return
    q=deque()
    q.append([a,b])
    cnt=1
    visited[a][b]=1
    
    while q:
        x,y=q.popleft()
        for k in range(0,4):
            dx=x+direc_x[k] # 세로
            dy=y+direc_y[k] # 가로 
        
            if 0<=dx<M and 0<=dy<N and visited[dx][dy]==0:
                # print(dx,dy)
                if war[dx][dy]==char:
                    cnt+=1
                    visited[dx][dy]=1 # 방문처리 해준다
                    q.append([dx,dy])
    if char=='W':
        result[0]+=cnt**2
    elif char=='B':
        result[1]+=cnt**2

for i in range(0,M): # 세로
    for j in range(0,N): # 가로
        if visited[i][j]==0 and war[i][j]=='W':
            bfs(i,j,'W')
        elif visited[i][j]==0 and war[i][j]=='B':
            bfs(i,j,'B')

for r in result:
    print(r,end=' ')

# 앞에가 세로 뒤가 가로


