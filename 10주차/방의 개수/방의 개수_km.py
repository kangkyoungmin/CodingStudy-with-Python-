# 방의 개수
# logic
# 1. 방향에 따른 x,y 설정 작업과, 이동 경로를 사전 자료형으로 정의하고
# results 배열로 들어온 값들을 확인하여 해당 노드들을 그어준다
# 즉 좌표와 노드를 함께 저장해준다
# 노드의 정방향,반대방향도 신경써준다
# 모래시계형을 통해 교차하는 것도 신경써준다 (노드량을 두 배로 늘린다)

# 2. bfs 방법을 통하여 첫 번째부터 돌면서 이전에 방문한 적이 있는 좌표이면서 
# 한번도 방문하지 않은 노드인 것을 찾아낸다

from collections import deque
dx=[0,1,1,1,0,-1,-1,-1]
dy=[1,1,0,-1,-1,-1,0,1]
def solution(arrows):
    answer=0
    # 사전형을 통한 노드,좌표 설정
    node,point,q={},{},deque()
    point[(0,0)]=0
    q.append([0,0])
    x,y=0,0

    for i in arrows:
        for _ in range(2): # 모래시계형을 고려해주기 위해 point를 두 배로 늘린다
            nx=x+dx[i] #x,y를 방향에 따라 늘려준다 
            ny=y+dy[i]
            point[(nx,ny)]=0 # 좌표값을 설정해준다
            q.append([nx,ny])
            node[(x,y,nx,ny)]=0
            node[(nx,ny,x,y)]=0
            x,y=nx,ny
    
    x,y=q.popleft()
    point[(x,y)]=1 # 맨 처음에는 1을 넣어준다
    while q:
        nx,ny=q.popleft()

        # 이전에 방문한 적이 있는 경우
        if point[(nx,ny)]==1:
            # 한 번도 방문한 적이 없는 노드인 경우
            if node[(x,y,nx,ny)]==0:
                answer+=1
                node[(x,y,nx,ny)]=1 # 노드를 방문한 것으로 바꿔준다
                node[(nx,ny,x,y)]=1
        else:
            # 이전에 방문한 적 없는 경우
            point[(nx,ny)]=1
            node[(x,y,nx,ny)]=1
            node[(nx,ny,x,y)]=1
        x,y=nx,ny

    return answer
print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))