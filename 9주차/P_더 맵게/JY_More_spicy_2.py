# programmers L2 : 더 맵게
# solved by JY
# DATE : 2021.03.09
# heapq 사용

import heapq

def solution(scoville, K):
    answer = 0
    pq = []
    for s in scoville:
        heapq.heappush(pq, s)

    while pq[0] < K:
        if len(pq) == 1:
            answer = -1
            break
        min1 = heapq.heappop(pq)
        min2 = heapq.heappop(pq)
        heapq.heappush(pq, min1 + (min2 * 2))
        answer += 1

    return answer

# run test
print(solution([2, 3, 1, 9, 10, 12], 7))    # 2
print(solution([0, 0], 7))    # -1
print(solution([1, 1, 1, 1, 1, 1], 10))    # -1