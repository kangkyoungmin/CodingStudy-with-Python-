# programmers L2 : 큰 수 만들기
# solved by JY
# DATE : 2021.01.12
# Greedy 알고리즘
# k가 남으면 뒤에 잘라냄

# best
def solution(number, k):
    stack = []
     
    for n in number:
        while stack and k > 0 and n > stack[-1] :
            k -= 1
            stack.pop()
        stack.append(n)

    if k > 0: return (''.join(stack[:-k]))
    return (''.join(stack))

# run test
# print(solution("1119", 2))
# print(solution("99919", 2))
print(solution("144444", 2))