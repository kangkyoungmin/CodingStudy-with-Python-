# N개의 정수 A[1] ... A[N]
# M개의 정수/ M이 A안에 존재? 존재O : 1 /존재X : 0

import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
L = list(map(int, sys.stdin.readline().split()))

A.sort()

def binary_search(A, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if A[mid] == target:
        return 1
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif A[mid] > target:
        return binary_search(A, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(A, target, mid+1, end)

for m in L:
    if binary_search(A, m, 0, N-1):
        print(1)
    else:
        print(0)
