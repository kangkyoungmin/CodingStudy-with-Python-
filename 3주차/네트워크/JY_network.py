# programmers L3 : 네트워크
# solved by JY
# DATE : 2020.01.21
# BFS 이용

def bfs(computers, visit, idx):
    que = [idx]
    while len(que) > 0:
        q = que[0]
        que.remove(q)
        visit[q] = 1

        for i in range(len(visit)):
            if visit[i] == 1 or computers[q][i] == 0:
                continue
            que.append(i)

def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]

    for i in range(n):
        if visit[i] == 0:
            bfs(computers, visit, i)
            answer += 1
    
    return answer

# run test
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))   # 2
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))   # 1