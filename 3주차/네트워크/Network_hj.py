def solution(n, computers):
    answer = 0  # 네트워크의 개수 저장할 곳
    bfs = []  # 탐색을 위한 큐
    visited = [0] * n  # 방문한 노드를 체크해 둘 리스트

    while 0 in visited: # vistied 리스트의 모든 값에 방문 표시가 되어있을 때까지 반복
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1  # 첫 노드 방문표시

        while bfs: # 큐의 값이 존재하면 반복문 수행
            node = bfs.pop(0)  # 큐의 앞에서부터 노드 꺼냄
            visited[node] = 1
            for i in range(n): # 꺼낸 노드의 인접 노드를 방문하기 위한 반복문 수행
                if visited[i] == 0 and computers[node][i] == 1:  # 인접 노드이고, 방문된 적 없는 경우
                    bfs.append(i) # 큐에 추가
                    visited[i] = 1
        answer += 1
    return answer

