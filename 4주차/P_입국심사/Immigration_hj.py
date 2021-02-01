def solution(n, times):
    start = 1 # 최소
    end = max(times) * n  # 최대 : 가장 오래걸리는 심사관이 n명 검사할 경우

    while start <= end:
        count = 0  # 심사 처리 수
        mid = (start + end) // 2  # 임의의 총 심사 시간

        # 각 심사대가 mid만큼의 시간이 주어졌을 때, 처리할 수 있는 최대 심사 인원 수
        # 모두 합해서 목표 심사 인원 n과 비교
        for i in range(len(times)):
            count += mid // times[i]

        # mid 시간동안 처리한 심사 인원 수가 n보다 크거나 같으면 end 변경
        # 한 심사관의 처리시간을 줄임
        if count >= n:
            answer = mid
            end = mid - 1
        else: # 작으면 start 변경
            start = mid + 1
    return answer
