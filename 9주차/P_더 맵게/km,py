import heapq
import timeit

def solution(scoville, K):
    start_time = timeit.default_timer() # 시작 시간 체크
    answer = 0
    check=0
    heapq.heapify(scoville)
    if scoville[0]>=K: # 최소값이 K보다 큰 경우
        return 0


    while len(scoville)>=2:
        first=heapq.heappop(scoville)
        second=heapq.heappop(scoville)
        temp=first+2*second
        answer+=1
        heapq.heappush(scoville,temp)
        
        if scoville[0]>=K:
            check=1
            break
    print(round((timeit.default_timer()-start_time),10))
    if check==0:
        return -1
    else:
        return answer
        

print(solution([1, 2, 3, 9, 10, 12]	,7))
