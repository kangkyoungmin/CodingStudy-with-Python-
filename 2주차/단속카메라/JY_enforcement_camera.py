# programmers L3 : 단속카메라
# solved by JY
# DATE : 2020.01.14
# Greedy 알고리즘
# 겹치는 구간에 카메라를 설치하면 되므로 겹치는 구간을 구함

def solution(routes):
    answer = 1
    routes.sort()
    check = routes[0]

    for r in routes[1:]:
        if check[1] >= r[0]:    # 겹치는 구간 구하기
            check[0], check[1] = r[0], min(check[1], r[1])
        else:                   # 겹치지 않음
            answer += 1
            check = r

    return answer

# run test
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))   # 2
# print(solution([[-20,-15], [-10,0], [5, 10]]))   # 3