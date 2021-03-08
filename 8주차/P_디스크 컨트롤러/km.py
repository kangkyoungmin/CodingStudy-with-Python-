# 요청 시간, 작업 진행 시간
# 작업 진행 순으로 정렬되어야 함
# 이 때 작업 요청 시간은 이전의 것보다 커야 함
# 작업 요청 시간이 이전 작업 시간보다 클 때는 시간을 흘려보낸다

# key point
# 작업 요청 시간이 이전 작업을 처리하는 도중 있으면 바로 이어서 진행된다
# 작업 요청 시간이 이전 작업을 처리하는 도중이 아니라면 요청 시간에 도달할 때까지 시간이 흐른다
import heapq
def solution(jobs):
    answer=0
    heap=[]
    heapq.heapify(heap)
    i=0
    start,now=-1,0
    current=0

    # 최소힙 기준으로 정렬시킨다
    
    
    while i<len(jobs):
        # 프로세스가 바로 이어져서 더해지는 경우
        for j in jobs:
            if start<j[0]<=now: # 요청 시간이 이전 것의 요청시간보다 크고 이전의 끝나는 시간보다 작아야 함
                heapq.heappush(heap,[j[1],j[0]]) # heap에 작업 진행 시간, 작업 요청 시간 순으로 넣는다
        # 프로세스가 바로 이어지지 못하는 경우 now의 조건을 만족할 때까지 계속 1씩 더해간다
        # 즉 이 경우는 끝난 프로세스보다 더 뒤에 요청시간이 있는 경우
        # start,now에 값을 할당해준다
        if len(heap)>0:
            current=heapq.heappop(heap)
            start=now
            now+=current[0]
            answer+=(now-current[1])
            i+=1
        else:
            now+=1
    return answer//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))

