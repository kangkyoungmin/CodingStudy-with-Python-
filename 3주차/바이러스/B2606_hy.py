N = int(input()) #컴퓨터의 수
network = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
virus_map = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 네트워크 정보 2차원 배열 안에 넣어주기. ->1과 연결된 것만 구하면 됨
for _ in range(network):
    x, y = map(int, input().split())
    virus_map[x][y] , virus_map[y][x] = 1, 1


# 1과 연결된 모든 노드 뽑기
def bfs(virus_map, start):
    queue = [start]
    visited = []

    while queue: # 큐 안에 원소들이 없어질 떄까지 반복
        temp = queue.pop(0) # 큐의 첫번째 원소 꺼냄
        visited.append(temp)

        for i in range(len(virus_map)): # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            if virus_map[temp][i] and i not in visited and i not in queue:
                queue.append(i)

    return len(visited) - 1 # 1번 컴퓨터는 빼줘야 함

# 1을 제외한 감염된 노드 수 출력
print(bfs(virus_map, 1))
