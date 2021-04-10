# baekjoon 1789 : 수들의 합
# solved by JY
# DATE : 2021.04.07
# 구현

import sys
input = sys.stdin.readline
S = int(input())
summ, i = 0, 1
while True:
    summ += i
    if summ >= S:
        if summ > S:    # summ - S인 값을 빼면 S가 됨
            i -= 1
        print(i)
        break
    i += 1
