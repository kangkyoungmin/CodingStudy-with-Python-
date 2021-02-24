# baekjoon 4195 : 친구 네트워크
# solved by JY
# DATE : 2021.02.23
# Union-Find 사용
# parent : { name, [부모, 친구 수] }

def find(p):    # 최상의 부모를 찾아서
    if p == parent[p][0]:
        return p
    parent[p][0] = find(parent[p][0])   # 최상의 부모로 부모 업데이트
    return parent[p][0]

def union(a, b):    # 그룹 합치기
    a_p, b_p = find(a), find(b)
    if a_p != b_p:  # 다른 그룹일 때 합치기
        parent[b_p][0] = a_p    # b_p의 그룹을 a_p그룹으로 변경. b_p는 더이상 최상의 부모가 아님!
        parent[a_p][1] += parent[b_p][1]    # a_p그룹에 b_p그룹의 친구 수 더해주기

# run test
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    F = int(input())
    parent = {}
    for _ in range(F):
        f1, f2 = input().split()

        if f1 not in parent:    
            parent[f1] = [f1, 1]
        if f2 not in parent:
            parent[f2] = [f2, 1]
        
        union(f1, f2)
        print(parent[parent[f1][0]][1]) # 부모의 친구 수 출력
        