# bfs를 사용하여 풀이한다
# 1이면 dfs를 돌려준다
# visited 배열을 정의하고 한번 다 돌고 나면 visited 배열을 0으로 만들어준다
from collections import deque
n=int(input())
visited=[]
for _ in range(n):
    visited.append(list(map(int,input())))
result=[]
# print(visited)
# 동서남북
dir_x=[1,-1,0,0]
dir_y=[0,0,-1,1]
def bfs(x,y):
    q=deque()
    q.append([x,y])
    num=0

    while q:
        x1,y1=q.popleft()
        if visited[x1][y1]==1:
            visited[x1][y1]=0 # 방문처리 한다
            num+=1 # 방문처리 할 떄마다 1씩 늘려준다
        for a in range(0,4):
            dx=x1+dir_x[a]
            dy=y1+dir_y[a]
            if 0<=dx<n and 0<=dy<n:
                if visited[dx][dy]==1 and [dx,dy] not in q:
                    q.append([dx,dy]) # q에 집어넣는다
                    # print([dx,dy])
    result.append(num)

cnt=0                    
for i in range(0,n):
    for j in range(0,n):
        if visited[i][j]==1:
            bfs(i,j)
            cnt+=1

print(cnt)
result.sort()
for r in result:
    print(r)



