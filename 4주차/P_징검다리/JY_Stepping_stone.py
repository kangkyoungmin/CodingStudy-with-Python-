# programmers L4 : 징검다리
# solved by JY
# DATE : 2021.02.01
# 이분탐색
# mid : 바위간의 거리의 최소값
# 테스트 케이스 2번만 실패 ㅠㅠ

def solution(distance, rocks, n):
    min_d, max_d = 1, distance
    rocks.sort()
    dist = [rocks[0]]
    for i in range(1, len(rocks)):
        dist.append(rocks[i] - rocks[i - 1])
    dist.append(distance - rocks[-1])

    while min_d < max_d:
        mid = (min_d + max_d) // 2
        cnt, tmp_dist = 0, dist[:]
        for idx in range(len(tmp_dist)):
            if tmp_dist[idx] < mid: # 바위를 제거한다.
                cnt += 1    # 돌 제거
                if idx + 1 < len(tmp_dist):
                    tmp_dist[idx + 1] += tmp_dist[idx]
            if cnt > n:  # 제거할 수 있는 바위 개수보다 많아지면 mid는 불가능한 답 > max_d 변경
                break

        if cnt > n:
            max_d = mid - 1
        else:           # mid가 가능하면 min_d 변경
            min_d = mid + 1

    return min_d - 1


# run test
print(solution(25, [2, 14, 11, 21, 17], 2))  # 4
# print(solution(42, [10, 20, 30, 40, 41], 1))  # 2
# print(solution(16, [4, 8, 11], 2))  # 8
