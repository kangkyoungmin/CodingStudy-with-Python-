# baekjoon 1541 : 잃어버린 괄호
# solved by JY
# DATE : 2021.03.24
# map 사용

import sys
input = sys.stdin.readline
calc = list(map(str, input().rstrip('\n').split('-')))  # -를 기준으로 split
calc = [sum(map(int, cal.split('+'))) for cal in calc]  # + 연산 수행
print((calc[0]*2) - sum(calc))