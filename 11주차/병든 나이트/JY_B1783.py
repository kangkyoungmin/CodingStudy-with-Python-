# baekjoon 1783 : 병든 나이트
# solved by JY + hint
# DATE : 2021.03.23
# 구현
# test : 3, 6 => 4

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

if N == 1 or M == 1:
    print(1)
elif N == 2:
    if M <= 2:
        print(1)
    else:
        print(min(M//2 + M % 2, 4))
else:
    if M <= 6:
        print(min(M, 4))
    else:
        print(M - 2)
