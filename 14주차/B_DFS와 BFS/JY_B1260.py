# baekjoon 1260 : DFS와 BFS
# solved by JY
# DATE : 2021.04.13
# DFS, BFS 알고리즘 사용

from sys import stdin
from collections import defaultdict
input = stdin.readline
N, M, V = map(int, input().split())
connect = defaultdict(set)
for _ in range(M):
    n1, n2 = map(int, input().split())
    connect[n1].add(n2)
    connect[n2].add(n1)

for key in connect:
    connect[key] = sorted(connect[key])

def dfs(v):
    print(v, end=' ')
    for i in connect[v]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i)

def bfs(v):
    que = [v]
    while que:
        v = que.pop(0)
        print(v, end=' ')
        for i in connect[v]:
            if visit[i] == 0:
                visit[i] = 1
                que.append(i)

for i in range(2):
    visit = [0]*(N+1)
    visit[V] = 1
    dfs(V) if i == 0 else bfs(V)
    print()