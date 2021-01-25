# 여행 경로

# 모든 공항은 알파벳 대문자 3글자로 이루어짐
# tickets의 각 행 [a,b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미

# visited 배열을 이용(도착지에 대한 정보를 visited 배열에 넣음)
# tickets[i][1]과 visited를 비교하여 없으면 visited에 추가하고 큐에 추가

# 너비 우선 탐색

# 인덱스 값을 visited로 두고 모든 것을 방문했을 때와

# def bfs(tickets):
#     queue=[]
#     visited=[]
#     for i,data in enumerate(tickets):
#         if data[0]=="ICN" and data[0]:
#             queue.append(data)
#             if data[0] not in visited:
#                 visited.append(data[0])

#     i=0
#     while queue: # 큐에 값이 있으면 
#         v=queue.pop() # 큐에서 하나를 pop
#         if v[1] in visited: # 꺼낸 것의 도착지가 이미 방문한 곳이라면
#             continue
#         for i in range(len(tickets)):         
#             if v[1]==tickets[i][0]: # 방문처리가 안되고 도착지에 출발지가 있을 때
#                 queue.append(data)
#                 if v[1] not in visited:
#                     visited.append(tickets[i][0])

# bfs([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

from collections import defaultdict
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        # 사전형으로 정의
        routes = defaultdict(list) # list형태로 사전형으로 정의된다.
        for key, value in tickets: # key,value 쌍으로 routes에 들어간다 # 해당 key값에 중복으로 데이터가 들어간다
            routes[key].append(value)
        return routes

    # 재귀 호출을 사용한 DFS
    def dfs(key, footprint): # key: 출발지 footprint: 발자취
        if len(footprint) == N + 1: # n번을 넘어가면 모두 return된다
            return footprint

        for idx, country in enumerate(routes[key]): #출발지에 해당하는 열에 있는 것
            routes[key].pop(idx)

            fp = footprint[:] # deepcopy 이게 하나의 핵심 deepcopy를 통해 재귀 구현
            fp.append(country) # 도착지 추가

            ret = dfs(country, fp)
            if ret: return ret # 모든 티켓을 사용해 통과한 경우 ret에 값이 존재하는 경우

            routes[key].insert(idx, country) # 통과 못했으면 티켓 반환

    routes = init_graph()
    for r in routes:
        routes[r].sort() # 예제2 알파벳 순으로 앞서는 것을 표현

    N = len(tickets)
    answer = dfs("ICN", ["ICN"])

    return answer

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])




