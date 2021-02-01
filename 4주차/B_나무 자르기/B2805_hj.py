# python3 시간초과, pypy 통과
import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

# 최소 높이 : 0, 최대 높이 : 가장 높은 나무
lowest = 0
highest = max(trees)
answer = 0

# 중간 높이로 모든 나무를 베었을 때 구할 수 있는 나무의 길이를 tree에 저장
# tree를 M과 비교
while lowest <= highest:
    mid = (lowest + highest) // 2
    tree = 0
    for i in range(N):
        if mid < trees[i]:
            tree += trees[i] - mid
    #높이 이분탐색
    # 나무가 원하는 길이 이상이면 mid+1을 lowest로 두고 while문 반복
    if tree >= M:
         answer = mid
         lowest = mid + 1
    # 나무가 원하는 길이 이하이면 mid-1을 highest로 두고 while문 반복
    else:
        highest = mid -1

print(answer)
