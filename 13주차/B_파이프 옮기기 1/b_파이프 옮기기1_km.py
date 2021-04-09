# 파이프 옮기기1

# 파이프는 회전시킬 수 있다. 
# 3가지 방향으로 가능하다
# 대각선 아래, 오른쪽, 아래방향
# 파이프는 항상 빈 칸만 차지해야 한다
# 회전은 45도만 가능, 미는 방향은 오른쪽 아래 또는 오른쪽 아래 대각선 방향
# 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있음

# 파이프의 한쪽 끝을 (n,n)으로 이동시키는 방법의 개수는?
# 파이프는 두 개의 연속된 칸을 차지하고 있따

# dfs 이용해서 풀어야 할 듯
# 가로, 세로, 대각선 방향 각각으로 가본다
import sys
n=int(sys.stdin.readline())
cnt=0 # 개수
# 오른쪽, 아래, 대각선
# 3가지 경우의 수가 존재한다
# 방향도 알고 있어야 함
# 가로이면 가로,대각선만
# 세로이면 세로,대각선만
# 대각선이면 가로,세로,대각선 모두 가능
# direc 0: 가로 1: 세로, 2: 대각선
direc_y=[1,0,1]
direc_x=[0,1,1]
# direc_z=[0,1,2]
visited=[list(map(int,input().split())) for _ in range(n)]
# print(visited)
tmp=2*n-3
def dfs(x,y,direc):
    global cnt
    if x>n or y>n: # 최대의 개수를 넘어가면 return 시켜준다
        return
    if x==n-1 and y==n-1: # x,y가 끝에 도달하면
        cnt+=1
        return

    if direc==0 or direc==2: # 가로일 떄
        dx=x+direc_x[0]
        dy=y+direc_y[0]
        if 0<=dx<n and 0<=dy<n and visited[dx][dy]==0:
            dfs(dx,dy,0) 

    if direc==1 or direc==2: # 세로일 때
        dx=x+direc_x[1]
        dy=y+direc_y[1]
        if 0<=dx<n and 0<=dy<n and visited[dx][dy]==0:
            dfs(dx,dy,1)

    if direc==0 or direc==1 or direc==2: # 대각선일 떄 
        if x+1<n and y+1<n: 
            if visited[x+1][y]==0 and visited[x][y+1]==0 and visited[x+1][y+1]==0:
                dx=x+direc_x[2]
                dy=y+direc_y[2]
                dfs(dx,dy,2)

dfs(0,1,0)

print(cnt)
                



