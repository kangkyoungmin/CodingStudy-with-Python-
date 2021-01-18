# programmers L3 : 섬 연결하기
# solved by JY
# DATE : 2020.01.13
# Greedy 알고리즘 - Kruskal 알고리즘(Union-Find 사용)
# 작은 비용부터 추가하며 수행
# 사이클이 생기는 다리는 추가하지 않음 
# (x, y가 같은 집합에 있는 정점일 경우 연결하면 사이클이 생김)


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def find(self, index):		# 최상위 부모 찾기
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]
    
    # 크기 비교해서 큰 집합에 작은 집합을 추가해야 더 효율적
    # 단순히 부모의 숫자가 더 작은 곳에 추가함
    def union(self, x, y):
        if self.parent[x] > self.parent[y]: self.parent[x] = y
        else: self.parent[y] = x


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])  # 비용 오름차순으로 정렬
    path = UnionFind(n)
    for c in costs:
        x, y = c[0], c[1]
        x_p, y_p = path.find(x), path.find(y)   # 정점의 부모 찾기
        
        if  x_p != y_p :    # 부모가 같지 않으면
            path.union(x_p, y_p)    # 집합 합치기
            answer += c[2]

    return answer
# run test
# print(solution(4, [[0,1,1],[0,2,3],[1,2,1],[1,3,1],[2,3,8]])) # 3
# print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]])) # 15

# print(solution(4 ,[[0,1,5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]] )) # 9
print(solution(4, [[0,1,1],[0,2,2],[2,3,1]])) # 4
# print(solution(, ))
# print(solution(, ))
# print(solution(, ))

