# programmers L3 : 가장 먼 노드
# solved by JY
# DATE : 2021.03.14
# bfs 사용
# 노드에 처음 도착하는 경우가 최단거리 성립

def solution(n, edge):
    connect = [[] for _ in range(n)]    # 각 노드마다 연결된 노드번호 저장
    for n1, n2 in edge:
        connect[n1-1].append(n2-1)
        connect[n2-1].append(n1-1)
    dist = [0] * n
    dist[0] = 1
    que = [0]
    while len(que) > 0:     # bfs
        node = que.pop(0)
        for n1 in connect[node]:
            if dist[n1] == 0:
                que.append(n1)
                dist[n1] = dist[node] + 1

    return dist.count(max(dist))

# run test
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)