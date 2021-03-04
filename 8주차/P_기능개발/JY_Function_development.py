# programmers L2 : 기능개발
# solved by JY
# DATE : 2021.03.04
# deque를 활용한 Queue 구조 사용

import math, collections

def solution(progresses, speeds):
    answer = []
    suc = collections.deque()

    for p, s in zip(progresses, speeds):
        suc.append(math.ceil((100-p)/s))    # 필요한 작업 기간 저장
    first, count = suc.popleft(), 1

    while len(suc) > 0:
        p = suc.popleft()

        if first >= p:      # 필요한 기간이 작으면 first와 함께 배포 가능 > count++
            count += 1
        else:               # 필요한 기간이 더 크면 배포하고 first가 p로 바뀜
            answer.append(count)
            first, count = p, 1

    answer.append(count)
    return answer

# run test
print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [2, 1]