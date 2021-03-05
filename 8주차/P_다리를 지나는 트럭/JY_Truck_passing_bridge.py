# programmers L2 : 다리를 지나는 트럭
# solved by JY
# DATE : 2021.03.05
# deque를 활용한 Queue 구조 사용

import collections

def solution(bridge_length, weight, truck_weights):
    answer = bridge_length
    que = collections.deque()
    que.append(truck_weights[0])
    w = truck_weights[0]
    idx = 1
    while len(que) > 0:
        if idx < len(truck_weights) and len(que) < bridge_length: # 트럭 추가 가능 조건1
            if weight >= w + truck_weights[idx]:   # 무게 조건2
                que.append(truck_weights[idx])
                w += truck_weights[idx]
                idx += 1
            else:                
                que.append(0)
        if len(que) == bridge_length or idx >= len(truck_weights):   # 트럭 추가 불가
            p = que.popleft()
            if p != 0:  # 트럭 빠짐. 무게 감소
                w -= p
            answer += 1

    return answer

# run test
print(solution(2, 10, [7,4,5,6]))   # 8
print(solution(100, 100, [10]))   # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))   # 110
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))   # 19