# programmers L2 : 프린터
# solved by JY
# DATE : 2021.03.05
# deque를 활용한 Queue 구조 사용

import collections

def solution(priorities, location):
    answer = 0
    idx, queue = collections.deque(), collections.deque()
    for i, p in enumerate(priorities):
        queue.append(p)
        idx.append(i)

    while len(queue) > 0:
        m = max(queue)
        if queue[0] == m:
            queue.popleft()
            answer += 1
            if idx.popleft() == location:
                break
        else:
            queue.append(queue.popleft())
            idx.append(idx.popleft())

    return answer

# run test
print(solution([2, 1, 3, 2], 2))    # 1
print(solution([1, 1, 9, 1, 1, 1], 0))    # 5