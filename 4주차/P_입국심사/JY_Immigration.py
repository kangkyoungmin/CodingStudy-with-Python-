# programmers L3 : 입국심사
# solved by JY
# DATE : 2021.02.01
# 이분탐색
# mid : 모든 사람이 심사를 받는데 걸리는 시간

def solution(n, times):
    min_t, max_t = 1, max(times)*n

    while min_t < max_t:
        mid = (min_t + max_t) // 2
        cnt = 0     # mid가 답일 때 검사받을 수 있는 사람의 수 확인
        for t in times:
            cnt += mid // t
            if cnt >= n:    # n보다 크면 mid 시간에 검사 가능 > max_t 변경
                break
        if cnt >= n:
            max_t = mid
        else:
            min_t = mid + 1
    return max_t


# run test
# print(solution(6, [7, 10]))  # 28
print(solution(10, [1, 5]))  # 9
