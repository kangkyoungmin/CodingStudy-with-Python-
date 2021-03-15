# n명의 권투선수가 권투 대회에 참여, 1번부터 n번까지 번호를 받았다
# 권투 경기는 1대1 방식으로 진행이 된다. 
# 정확하게 순서를 매길 수 있는 선수의 수는?
# [a.b]이면 a가 승리, b가 패배라는 의미이다.
# bfs를 통해서 파고 들어가면 된다
# visited 배열을 기존 result 순위 배열
# visited 배열 안에 들어가 있는 것 외에 다른 것과의 결과가 있어야 함
# bfs를 통하여 5위부터 visited 배열 안에 집어넣어준다
# process
# 초기에 정렬 작업을 어떻게 해 줄 것인가?
# 

# 1. 이긴 것들로 정렬하기
def solution(n, results):
    answer = 0
    w_list=[set() for _ in range(n+1)]
    l_list=[set() for _ in range(n+1)]

    for r in results:
        w_list[r[0]].add(r[1])
        l_list[r[1]].add(r[0])

    for i in range(1,n+1):
        for win in l_list[i]:
            w_list[win].update(w_list[i])
        for lose in w_list[i]:
            l_list[lose].update(l_list[i])


    # w_list는 이긴 것들의 집합
    # l_list는 진 것들의 집합

    for i in range(1,n+1):
        if len(w_list[i])+len(l_list[i]) == n-1:
            answer+=1

    return answer




print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))