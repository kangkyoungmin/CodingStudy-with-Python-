# baekjoon 14888 : 연산자 끼워넣기
# solved by JY
# DATE : 2021.03.29
# 재귀 사용, 모든 경우를 확인

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
calc = list(map(int, input().split()))
maxi, mini = float('-inf'), float('inf')

def rec(num, idx):
    if idx == N-1:
        global maxi, mini
        maxi, mini = max(maxi, num), min(mini, num)
        return

    if calc[0] != 0:
        calc[0] -= 1
        rec(num + A[idx+1], idx+1)
        calc[0] += 1
    if calc[1] != 0:
        calc[1] -= 1
        rec(num - A[idx+1], idx+1)
        calc[1] += 1
    if calc[2] != 0:
        calc[2] -= 1
        rec(num * A[idx+1], idx+1)
        calc[2] += 1
    if calc[3] != 0:
        calc[3] -= 1
        if num < 0 and A[idx+1] > 0:
            rec(-((-num)// A[idx+1]), idx+1)
        else:
            rec(num // A[idx+1], idx+1)
        calc[3] += 1

rec(A[0], 0)
print(maxi,mini, sep='\n')
