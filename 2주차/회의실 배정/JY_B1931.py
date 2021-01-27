# baekjoon 1931 : 회의실 배정
# solved by JY
# DATE : 2021.01.17
# Greedy 알고리즘

def solution():
    answer = 1
    pre_end = con[0][1]
    for cur in con[1:]:
        if pre_end <= cur[0]:
            answer += 1
            pre_end = cur[1]
    return answer

# run test
n = int(input())
con = [list(map(int, input().split())) for _ in range(n)]
con.sort(key=lambda x: (x[1], x[0]))    # 끝나는 시간 기준으로 정렬, 동일 시 시작 오름차순
print(solution())