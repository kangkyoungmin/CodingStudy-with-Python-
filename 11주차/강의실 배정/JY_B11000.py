# baekjoon 11000 : 강의실 배정
# solved twice by JY
# DATE : 2021.03.26
# Greedy 알고리즘, heapq 사용

import sys, heapq
input = sys.stdin.readline
N = int(input())
lessons = [list(map(int, input().split())) for _ in range(N)]
lessons = sorted(lessons, key=lambda x:(x[0],x[1]))
cnt = [lessons[0][1]]
heapq.heapify(cnt)
for lesson in lessons[1:]:
    if cnt[0] <= lesson[0]:
        heapq.heappop(cnt)   
    heapq.heappush(cnt,lesson[1])
    
print(len(cnt))
    
