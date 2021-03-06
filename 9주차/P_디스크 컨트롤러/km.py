# 하드디스크는 한 번에 하나의 작업만 수행가능
# 다양한 순서로 묶어낼 수 있다
# 이 때 요청된 시점부터 종료된 시점까지의 차를 모두 더한 것의 평균치가 가장 낮은 것은?

# sol
# 현재 시점에서 처리할 처리할 때까지 반복한다.
# 힙에 push를 할 때는 작업의 소요 시간 기준으로 최소힙이 만들어져야 하기 때문에 jobs의 요소를 그대로 넣지 않고 수 있는 작업들을 힙에 넣고, 하나를 뽑아 현재 시점과 총 대기시간을 구해주는 것을 모든 작업을 [작업의 소요 시간, 작업이 요청되는 시점]으로 요소의 앞 뒤를 바꿔서 넣어준다.
# 현재 시점에서 처리할 수 있는 작업인지를 판별하는 조건은 작업의 요청 시간이 바로 이전에 완료한 작업의 시작 시간(start)보다 크고 현재 시점(now)보다 작거나 같아야 한다.
# 만약 현재 처리할 수 있는 작업이 없다면, 남아 있는 작업들의 요청 시간이 아직 오지 않은 것이기 때문에 현재 시점(now)을 하나 올려준다.

import heapq

def solution(jobs):
    answer = 0
    now=0
    heap=[] 
    i=0
    start=-1
    heapq.heapify(heap) # 힙 생성
    

    while i<len(jobs):
        for j in jobs:
            if start<j[0]<=now: #요청시간이 바로 이전의 시작 시간보다 크고 현재 시간보다 작아야 한다
                heapq.heappush(heap,[j[1],j[0]]) # jobs에 있는 힙을 넣어주는데 이 때 process time 기준으로 최소힙으로 만들어준다
        if len(heap)>0: # heap의 크기가 0보다 클 때
            current=heapq.heappop(heap) #최소힙을 통해 구현한 최소 처리시간이 걸리는 것을 current로 뽑아낸다
            start=now # 현재시간으로 start의 값을 변경한다
            now+=current[0] # 처리시간들이 더해진다
            answer+=(now-current[1]) # 현재시간-요청시간을 통하여 answer을 구한다
            i+=1
        else:
            now+=1
    return answer//len(jobs)

            # 현재 시점에서 처리할 수 있는 작업인지의 판단
print(solution([[0, 3], [1, 9], [2, 6]]))

# FCFS 방법: 먼저 들어오는 작업을 먼저 수행하는 것
# 긴 작업이 먼저 들어올 경우 들어온 작업들이 수행하기까지 많은 시간을 대기하기 때문에 평균시간이 길어지게 된다
# 이를 해결하기 위해 SJF를 사용한다
# 즉 짧은 요청을 먼저 수행하는 것이다
# 이 때 별도의 정렬없이 들어옴과 동시에 정렬을 수행하는 힙 자료구조를 사용하는 것이 좋다


