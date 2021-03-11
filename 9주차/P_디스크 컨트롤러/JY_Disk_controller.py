# programmers L3 : 디스크 컨트롤러
# solved by JY
# DATE : 2021.03.09
# heapq 사용
# pre_end = 이전 수행한 작업이 끝난 시간
# pq_e = pre_end 시간 전에 요청된 작업이 담긴 pq

import heapq

def solution(jobs):
    jobs.sort()
    answer, pre_end, idx = 0, 0, 0
    pq_e = []
    
    while len(pq_e) > 0 or idx < len(jobs):
        if len(pq_e) == 0:  # 요청시간 제일 빠른 작업 수행
            start, time = jobs[idx]
            pre_end = start + time
            answer += time
            idx += 1
        else:  # 소요시간이 가장 적은 작업 수행
            time, start = heapq.heappop(pq_e)
            pre_end += time
            answer += pre_end - start

        tmp_job = jobs[idx:]
        for start, time in tmp_job: # pre_end 시간 전에 요청된 작업이 존재 시 pq_e에 추가
            if pre_end < start:
                break
            heapq.heappush(pq_e, (time, start))
            idx += 1

    return answer//len(jobs)

# run test
print(solution([[0, 3], [2, 6], [1, 9]]), 9)
print(solution([[2, 3], [6, 3]]), 3)
print(solution([[0, 9], [1, 2]]), 9)
print(solution([[0, 9], [1, 2]]), 5)
print(solution([[0, 9], [8, 3], [8, 5]]), 7)
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14) ##
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25) 
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 550)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)