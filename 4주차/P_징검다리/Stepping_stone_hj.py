
# 이분탐색의 기준 : 바위 사이의 거리
# - 바위끼리 사이의 거리가 이분탐색 기준값보다 작을 경우 뒤쪽 돌 삭제
# - 삭제한 바위의 개수가 기준n보다 클 경우 바위 사이의 거리를 줄이고,
#   n보다 작거나 같을 경우 거리를 늘림

import math
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start, end, N = 0, distance, len(rocks)
    answer = 0

    while start <= end:
        prev = 0 # 이전 돌
        mins = math.inf # 무한대값,돌 거리의 최솟값 구하기 위한 초기값 넣어둠
        removed_rocks = 0 # 제거한 돌의 개수
        mid = (start + end) // 2 # 바위 사이의 최소 거리

        for i in range(N): # 제거할 돌 찾기
            if mid > rocks[i] - prev:
                removed_rocks += 1
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]
        # 제거한 돌 개수가 기준보다 많으면 바위 제거를 줄여야 함 -> 바위 사이 최소거리의 기준 낮춤
        if removed_rocks > n:
            end = mid - 1
        else: # 기준보다 적으면 더 많은 바위 제거 필요
            answer = mins
            start = mid + 1
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))

# 참고 https://deok2kim.tistory.com/122
# https://inspirit941.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-Level-4
