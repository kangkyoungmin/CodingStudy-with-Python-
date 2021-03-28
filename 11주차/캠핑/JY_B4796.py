# baekjoon 4796 : 캠핑
# solved by JY
# DATE : 2021.03.24
# Greedy

import sys
input = sys.stdin.readline
case = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0:
        break
    ans = (V//P)*L
    ans += V%P if V%P <= L else L

    print("Case %d: %d"%(case, ans))
    case += 1
