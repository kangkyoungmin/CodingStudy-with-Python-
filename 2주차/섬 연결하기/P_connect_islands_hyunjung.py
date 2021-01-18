# programmers L3 : 섬 연결하기
# DATE : 2020.01.18
# Greedy 알고리즘


# Kruskal 알고리즘
# 최소 신장 트리(MST)
# 사이클을 이루지 않고, 최소 비용을 찾는 것
# 탐욕적인 방법을 이용하여 간선에 할당한 그래프의 모든 정점을 최소 비용으로 연결하는 최적의 해답 구함
# 노드를 모두 연결하는 최소 비용의 간선을 파악 -> 가중치 작은 간선부터 탐색하도록 정렬
# # 이미 경로가 되어있는 곳에서 사이클이 만들어질 경우 그 간선은 선택하지 않음


#1. 그래프의 간선들을 오름차순으로 정렬
#2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선 선택
#3. 해당 간선을 현재의 집합에 추가(union-find 알고리즘)
# ex) [{1}, {2}] ⇨ 간선(3, 4)추가  ⇨ [{1}, {2}, {3}, {4}]
# ⇨ 간선(2, 5) 추가 ⇨ [{1}, {2, 5}, {3}, {4}]
# ⇨ 간선(1, 2) 추가 ⇨ [{1, 2, 5}, {3}, {4}]

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준 오름차순
    connection = [costs[0][0]] # 가장 비용작은 섬(노드) 넣음/ connection : 방문 확인하는 리스트
    while len(connection) != n:
        for i, cost in enumerate(costs):
            # 반복문을 돌면서 섬 확인
            # 이미 두 노드가 존재함 -> 넘어감
            if (cost[0] in connection) and (cost[1] in connection): continue
            # 둘 중 하나만 connection에 있을 경우 -> answer에 비용더해줌, connection에 해당 섬에 대한 정보 추가
            if (cost[0] in connection) or (cost[1] in connection):
                answer += cost[2]
                connection.append(cost[0])
                connection.append(cost[1])
                # connection = list(set(connection)) # 중복제거
                costs.pop(i)
                break
    return answer


# Union-Find 란 Disjoint Set 을 표현할 때 사용하는 독특한 형태의 자료구조로,
#    공통 원소가 없는, 즉 "상호 배타적" 인 부분 집합 들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
#    입니다.
# 위의 상황을 표현하기 위해서는 초기화 과정과 다음과 같은 두 가지 연산을 지원해야 하기 때문에, Union-Find 자료구조 라고 부르게 되었다고 합니다.



# Union-Find 지원 연산
# 초기화 : N 개의 원소가 각각의 집합에 포함되어 있도록 초기화 합니다.
# Union (합치기) 연산 : 두 원소 a, b 가 주어질 때, 이들이 속한 두 집합을 하나로 합칩니다.
# Find (찾기) 연산 : 어떤 원소 a 가 주어질 때, 이 원소가 속한 집합을 반환합니다.
# https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html
