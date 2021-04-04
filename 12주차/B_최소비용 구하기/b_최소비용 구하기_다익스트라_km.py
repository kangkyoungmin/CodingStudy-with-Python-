
import heapq
# N개
N=int(input()) # 도시의 개수
M=int(input()) # 버스의 대수

# 플로이드-워셜 알고리즘을 적용하거나 다익스트라 알고리즘 적용
# bus=[[float('inf')]*N for _ in range(N)]
# for _ in range(M):
#     i,j,k=map(int,input().split())
#     bus[i-1][j-1]=k
# start,end=map(int,input().split())
# print(bus)

#사전형의 형태로 정의한다

def diekstra(bus,start,end):
    q=[]
    dist=[float('inf')]*N
    dist[start-1]=0
    heapq.heappush(q, [start-1,0])  # 시작 노드부터 탐색 시작 하기 위함.

    while q:
        city,current_distance=heapq.heappop(q) # 시작 도시와 거리를 받는다

        for arrive,cnt in bus[city]: 
            cnt+=current_distance # 현재 거리를 더 해준다 (예: A->B->C)
            if cnt<dist[arrive]: # 기존의 (예 A->C)인 경우와 비교 
                dist[arrive]=cnt
                heapq.heappush(q,[arrive,cnt]) # 거쳐서 가는 경우가 더 나은 경우 heap에 푸쉬해준다

    return dist[end-1]

bus=[[] for _ in range(N)]
for _ in range(M):
    i,j,k=map(int,input().split())
    bus[i-1].append([j-1,k])
start,end=map(int,input().split())
print(diekstra(bus,start,end))



