# programmers L2 : 주식가격
# solved by JY
# DATE : 2021.03.04
# list를 활용한 stack 구조 사용

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    top = 0

    for p in prices:
        if len(stack) == 0:
            stack.append(p)
        else:
            top = len(stack) - 1
            count = 0       # 초를 확인하기 위한 변수
            while len(stack) > 0:
                if stack[top] == 0:
                    top -= 1
                    count += 1
                    if top >= 0:
                        continue
                if top < 0 or stack[top] <= p:  # 유지 및 상승일 경우
                    stack.append(p)
                    break
                else:                   # 떨어지는 경우
                    count += 1          # 초 추가
                    stack[top] = 0      # 가격을 0으로 변경
                    answer[top] = count
                    top -= 1

    top = len(answer) - 1
    count = 0
    while len(stack) > 0:   # stack 빼면서 초 세기
        p = stack.pop()
        if p != 0:
            answer[top] = count
        count += 1
        top -= 1

    return answer

# run test
# print(solution([1, 2, 3, 2, 3]))    # [4, 3, 1, 1, 0]
print(solution([5,6,7,5,6,4]))    # [5,2,1,2,1,0]