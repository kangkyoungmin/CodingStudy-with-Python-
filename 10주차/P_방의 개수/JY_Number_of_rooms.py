# programmers L5 : 방의 개수
# solved by JY + hint
# DATE : 2021.03.17
# 방이 생기는 경우
# 1. 연결된 선이 있는 점에 새로운 선으로 들어온 경우
# 2. 대각선으로 가는 새로운 선과 크로스되는 대각선 선이 존재하는 경우

#      0,  1, 2, 3, 4,  5,  6,  7
dx = [ 0,  1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1,  1,  0, -1]
check = {1:7, 3:5, 5:3, 7:1}
from collections import defaultdict

def solution(arrows):
    answer = 0
    line = defaultdict(set)
    x, y = 0, 0
    for arrow in arrows:
        if arrow % 2 == 1 and arrow not in line[(y,x)]:  # 대각선
            if arrow < 4 and check[arrow] in line[(y, x+1)]:    # arrow : 1, 3
                answer += 1
            if arrow > 4 and check[arrow] in line[(y, x-1)]:    # arrow : 5, 7
                answer += 1
        line[(y, x)].add(arrow)
        x += dx[arrow]
        y += dy[arrow]
        
        if len(line[(y, x)]) != 0 and (arrow+4)%8 not in line[(y, x)]:
            answer += 1
        line[(y, x)].add((arrow+4)%8)

    return answer

# run test
print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]), 3)
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]), 3)
print(solution([5, 2, 7, 1, 6, 3]), 3)
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]), 3)