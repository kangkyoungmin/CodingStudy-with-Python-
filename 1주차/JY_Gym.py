# programmers L1 : 체육관
# solved by JY
# DATE : 2020.01.11
# Greedy 알고리즘

def solution(n, lost, reserve):
    answer = n

    re = set(reserve) - set(lost)
    lo = set(lost) - set(reserve)

    for i in re:
        if i - 1 in lo:
            lo.remove(i - 1)
        elif i + 1 in lo:
            lo.remove(i + 1)

    return answer - len(lo)

# run test
n = 3
lost = [1, 2]
reserve = [2, 3]
print(solution(n, lost, reserve))
