# baekjoon 2606 : 바이러스
# solved by JY
# DATE : 2021.01.19
# BFS

import sys
import collections
def BFS():
    deq = collections.deque()
    deq.append(1)

    while len(deq) > 0:
        c = deq.popleft()
        
        for i in com[c-1]:
            if i not in visit:
                visit.add(i)
                deq.append(i)
# run test
C, N = int(sys.stdin.readline().rstrip()), int(sys.stdin.readline().rstrip())
com = [[] for i in range(C)]
visit = set()
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    com[a - 1].append(b)
    com[b - 1].append(a)
BFS()
print(len(visit) - 1)