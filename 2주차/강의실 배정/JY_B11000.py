# baekjoon 11000 : 강의실 배정
# solved by JY
# DATE : 2021.01.18
# Greedy 알고리즘
# heapq를 이용하여 최소힙으로 구현
# PyPy3으로 채점, Python으로 채점 시 시간초과 발생

import heapq

def solution():
    room = []
    heapq.heappush(room, time[0][1])
    for cur in time[1:]:
        if room[0] <= cur[0]:    # 같이 들을 수 있음
            heapq.heappop(room)
        heapq.heappush(room, cur[1])
    return len(room)
# run test
n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()
print(solution())