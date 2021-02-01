# baekjoon 12015 : 가장 긴 증가하는 부분 수열 2
# solved by JY
# DATE : 2021.02.01
# 이분탐색
# bisect_left(arr, a) : arr 배열에서 a 값의 index를 반환
# a가 없으면 a보다 가장 가까운 큰 수의 index를 반환
# 모든 원소가 a보다 작으면 len(arr)을 반환
import sys
from bisect import bisect_left

def solution():
    answer = [] # 증가하는 수 
    for a in A:
        # 비어있거나 top보다 클 경우 추가
        if not answer or a > answer[-1]:
            answer.append(a)
        else:   # a의 위치를 찾아 값 변경
            answer[bisect_left(answer, a)] = a

    print(len(answer))

# run test
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split(" ")))
solution()
