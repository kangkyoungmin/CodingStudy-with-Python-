# baekjoon 1197 : 최소 스패닝 트리
# solved by JY
# DATE : 2021.04.04
# Greedy 알고리즘 - Kruskal 알고리즘(Union-Find 사용)

import sys
input = sys.stdin.readline
V, E = map(int, input().split())
dists = []
for idx in range(E):
    dists.append(list(map(int, input().split())))
dists = sorted(dists, key=lambda x : x[2])
parent, rank = [0]*(V + 1), [0]*(V + 1)
for idx in range(1, V+1):
    parent[idx] = idx

def find(idx):
    if parent[idx] != idx:
        parent[idx] = find(parent[idx])
    return parent[idx]

def union(x, y):
    if rank[x] > rank[y]: parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

ans = 0
for dist in dists:
    s, e, w = dist
    ps, pe = find(s), find(e)
    if ps != pe:
        union(ps, pe)
        ans += w

print(ans)

