# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
# 더 이상 방문할 수 없는 점이 없는 경우 종료

# 입력으로 주어지는 간선은 양방향

import sys
from collections import deque
#정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
N,M,V=map(int,sys.stdin.readline().split())
point=[]
point=[[] for _ in range(N)]

# input
for i in range(0,M):
    n,m=map(int,input().split())
    point[n-1].append(m)
    point[m-1].append(n)

# sort
for j in range(0,N):
    point[j].sort()

# output
def output(result):
    for r in result:
        print(r,end=' ')


visited=[V]
result=[V]
# print(point)
def dfs(num):
    if len(result)==N:
        return

    for d in point[num-1]:
        if d not in visited:
            visited.append(d)
            if len(result)!=N:
                result.append(d)
            dfs(d)
dfs(V)
# print(result)
output(result)
# print(point)
result=[V]
visited=[V]

def bfs(num):

    q=deque()
    q.extend(point[num-1])
    tmp=0

    while q:
        tmp=q.popleft() # q에서 한 개씩 빼준다
        visited.append(tmp)
        result.append(tmp)
        # visited.append(tmp) # 방문처리해준다
        for t in point[tmp-1]:
            if t not in visited and t not in q:
                q.append(t)
                 
bfs(V)
# print(result)
print()
output(result)
        
    





    


