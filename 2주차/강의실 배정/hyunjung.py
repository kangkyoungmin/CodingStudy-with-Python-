# Baekjoon Online Judge : 강의실 배정
# DATE : 2020.01.17
# Greedy 알고리즘


# pypy3로 하면 통과 / Python3으로 하면 시간초과



# heap : 데이터에서 최대값과 최소값을 빠르게 찾기 위해 만들어진 완전 이진트리
# Root에 최대값이 있는 최대힙, 최소값이 있는 최소힙
# 최대힙의 경우 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 커야 함 / 최소힙은 반대
# 힙의 원리(최소힙 기준)
#   - 값을 하나씩 트리의 노드에서 좌에서 우로 할당
#   - 부모노드의 값이 자식노드보다 크면 부모와 자식 교체
#   - 루트노드까지 비교 반복

# heapq 모듈 : 보통 리스트를 최소 힙처럼 다룰 수 있도록 도와주는 모듈
# 따라서 빈 리스트 생성 후 heapq모듈의 함수 호출 시 리스트를 인자로 넘겨 최소 힙 자료구조로 동작
# heapq 모듈을 이용해 원소를 추가, 삭제한 리스트는 최소 힙(최소값이 인덱스0에 나타남)
# 힙 : https://www.daleseo.com/python-heapq/

# heapq.heappush : 힙에 원소 추가
# heapq.heappop : 힙에서 원소 삭제
# heapq.heapify() : 기존 리스트를 힙으로 변환


import heapq
N = int(input())
time = [list(map(int, input().split())) for i in range(N)]
li = [] # 강의실

# 강의를 빨리 시작하는 순서대로 정렬
time.sort(key=lambda  x:x[0])
for i in range(N):
    if len(li) != 0 and li[0] <= time[i][0]: # 가장 빨리끝나는 시간 <= 다음 강의 시작하는 시간
        heapq.heappop(li) # 같은 강의실을 쓰는 것이므로 최소힙 빼줌
    heapq.heappush(li, time[i][1]) # 끝나는 시간 삽입

print(len(li))

# ex) [(1,3), (2,4), (3,5)] /2




# Fail - 끝나는 시간 기준 풀이

# import heapq
# # heapq 모듈 : 보통 리스트를 최소 힙처럼 다룰 수 있도록 해줌
#
# N = int(input())
# time = [list(map(int, input().split())) for i in range(N)]
# time.sort(key=lambda  x:(x[1],x[0])) # 끝나는 시간 오름차순 -> 시작시간 오름차순
#
# q = []
# heapq.heappush(q,time[0][1])
# # 최대한 빨리 끝나는 강의 순서대로 정렬, 우선순위큐에 push
#
# for i in range(1, N):
#     if q[0] <= time[i][0]:
#         heapq.heappop(q)
#     heapq.heappush(q,time[i][1])
#
# print(len(q))

