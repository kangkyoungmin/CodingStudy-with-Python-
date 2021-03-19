# programmers L3 : 합승 택시 요금
# solved by JY
# DATE : 2021.03.18
# 플로이드 워샬 알고리즘

def solution(n, s, a, b, fares):
    answer = INF = float('inf')
    node = [[INF] * n for _ in range(n)]
    for i in range(n):          # 대각선
        node[i][i] = 0

    for n1, n2, c in fares:     # 이용 요금 정보 추가
        node[n1-1][n2-1] = c
        node[n2-1][n1-1] = c
    
    for k in range(n):          # 중간 노드
        for i in range(n):
            for j in range(n):
                if node[i][j] > node[i][k] + node[k][j]:
                    node[i][j] = node[i][k] + node[k][j]

    for s1,a1,b1 in zip(node[s-1], node[a-1], node[b-1]):
        answer = min(answer, s1+a1+b1)

    return answer

# run test
print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]),82)
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]),14)
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]),18)