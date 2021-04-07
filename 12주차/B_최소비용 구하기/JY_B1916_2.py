# baekjoon 1916 : 최소비용 구하기
# solved by JY
# DATE : 2021.04.04
# 다익스트라 알고리즘 이용

import sys, collections, heapq
input = sys.stdin.readline
N, M = int(input()), int(input())
dic = collections.defaultdict(list)
for idx in range(M):
    s, e, c = map(int, input().split())
    dic[s].append([e,c])

scity, ecity = map(int, input().split())
INF = float('inf')
visit = [INF]*(N+1)
visit[scity] = 0
pq = []
heapq.heappush(pq, [0, scity])

while pq:
    cost, cur = heapq.heappop(pq)
    if visit[cur] < cost:
        continue
    if cur == ecity:
        break
    for nextcity, nextcost in dic[cur]:
        if visit[nextcity] > cost + nextcost:
            visit[nextcity] = cost + nextcost
            heapq.heappush(pq, [cost + nextcost,nextcity])

print(visit[ecity])
