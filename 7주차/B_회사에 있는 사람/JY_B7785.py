# baekjoon 7785 : 회사에 있는 사람
# solved by JY
# DATE : 2021.02.23
# dictionary를 활용한 구현

# run test
import sys
input = sys.stdin.readline
n = int(input())
enter = {}
for i in range(n):
    name, inout = map(''.join, input().rstrip('\n').split(" "))
    if name not in enter:   # set에 없으면 enter
        enter[name] = inout
    else:                   # set에 존재하면 leave
        enter.pop(name)

enter = list(enter)         # sort를 위한 list 변환
enter.sort(reverse=True)    # 역으로 sort
for e in enter:
    print(e)
