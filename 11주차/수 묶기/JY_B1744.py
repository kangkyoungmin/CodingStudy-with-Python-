# baekjoon 1744 : 수 묶기
# solved by JY
# DATE : 2021.03.25
# Greedy

import sys, bisect
input = sys.stdin.readline
N = int(input())
nums = [0]*N
for idx in range(N):
    nums[idx] = int(input())
nums = sorted(nums)
idx, ans = 0, 0

while idx + 1 < N:          # 음수 부분 처리
    if nums[idx+1] <= 0:
        ans += nums[idx]*nums[idx+1]
        idx += 2
        continue
    if nums[idx] <= 0:      # nums[idx+1]은 무조건 양수
        ans += nums[idx]
        idx += 1
    break

# 양수 부분(idx부터)
while idx < N and nums[idx] == 1:   # 1은 그냥 더하는 게 좋음
    ans += nums[idx]
    idx += 1

if idx < N and (N - idx)%2 == 1:    # 양의 정수가 홀수 개일 경우
    ans += nums[idx]
    idx += 1

while idx + 1 < N:
    ans += nums[idx]*nums[idx+1]
    idx += 2

print(ans)
        
