# programmers L2 : H-Index
# solved by JY
# DATE : 2021.02.06
# 정렬. sort() 이용
# 역순 정렬 후 idx+1이 현재까지 확인한 논문 개수이므로
# idx+1보다 인용횟수가 더 클 경우 H-Index 만족

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx in range(len(citations)):
        if citations[idx] >= idx + 1:
            answer = idx + 1
        else:
            break

    return answer

# run test
import sys
input = sys.stdin.readlines
print(3, 2, 0)
print(solution([3, 0, 6, 1, 5]), end=' ')
print(solution([6, 6, 0]), end=' ')
print(solution([0, 0, 0]), end=' ')