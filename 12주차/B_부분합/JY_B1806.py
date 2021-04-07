# baekjoon 1806 : 부분합
# solved by JY
# DATE : 2021.04.03
# 투 포인터 사용

import sys
input = sys.stdin.readline
N, S = map(int, input().split())
num = list(map(int, input().split()))
summ, cnt = 0, float('inf')
start, end = 0, 0
while start < N and end <= N:
    if summ < S:
        if end < N:
            summ += num[end]
            end += 1
        else:
            break
    else:
        cnt = min(cnt, end-start)
        summ -= num[start]
        start += 1
        
if cnt == float('inf'):
    cnt = 0
print(cnt)