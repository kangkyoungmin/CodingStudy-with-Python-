# 백준 2606번

from collections import deque
n=int(input())
iter=int(input())

computer=[[] for _ in range(n)] # computer간의 연결 관걔
visited=[0]*n
visited[0]=1
for i in range(0,iter):
    a,b=map(int,input().split())
    computer[a-1].append(b-1)
    computer[b-1].append(a-1)

direc_x=[1,0,0,-1] # 아래, 오른쪽, 위, 왼쪽
direc_y=[0,1,-1,0]
count=-1
def bfs(num):
    q=deque()
    q.append(num)
    global count
    while q:
        number=q.popleft()
        count+=1 
        for j in computer[number]:
            if number in computer[j] and visited[j]==0: # 양방향 연결
                q.append(j)
                visited[j]=1

bfs(0)
print(count)



