# baekjoon 10610 : 30
# solved by JY + hint
# DATE : 2021.03.23
# 구현
# 3의 배수는 각 수를 더한 값이 3으로 나누어 떨어진다.

import sys
input = sys.stdin.readline
N = list(map(int, input().rstrip()))
def solution():
    if 0 not in N:
        return -1
    n = sorted(N, reverse=True)
    if sum(n)%3 == 0:
        return ''.join(list(map(str, n)))
    return -1

print(solution())