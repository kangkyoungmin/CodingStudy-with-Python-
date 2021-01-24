# programmers L2 : 타겟 넘버
# solved by JY
# DATE : 2020.01.21
# 재귀 이용

def f(numbers, target, idx, mysum):
    if idx == len(numbers):
        return 1 if mysum == target else 0

    return f(numbers, target, idx + 1, mysum + numbers[idx]) + f(numbers, target, idx + 1, mysum - numbers[idx])

def solution(numbers, target):
    return f(numbers, target, 0, 0)


# run test
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))