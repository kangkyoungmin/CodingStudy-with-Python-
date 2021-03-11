# programmers L3 : 이중우선순위큐
# solved by JY
# DATE : 2021.03.11
# heapq 사용

import heapq

def solution(operations):
    hq = []
    for op in operations:
        if op[0] == 'I':    # I
            heapq.heappush(hq, int(op[2:]))
        else:               # D
            if len(hq) == 0:
                continue
            if op[2] == '-':
                heapq.heappop(hq)
            else:
                hq.remove(max(hq))

    return [max(hq), heapq.heappop(hq)] if len(hq) > 0 else [0,0]

# run test
print(solution(["I 16","D 1"]), [0,0])
print(solution(["I 7","I 5","I -5","D -1"]), [7,5])
print(solution(["I 5", "I 5", "D 1", "I 7", "D -1", "I 8"]), [8,7])
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]), [333,-45])
	

