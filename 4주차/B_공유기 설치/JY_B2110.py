# baekjoon 2110 : 공유기 설치
# solved by JY
# DATE : 2021.01.31
# 이분탐색
# mid : 인접한 두 공유기 사이의 거리

def check(mid) :    # mid가 답이라고 가정할 때 문제의 조건을 만족하는 지 확인
    cnt, s = 1, house[0]
    for idx in range(1,N):
        if house[idx] - s >= mid:       # 집간의 거리가 mid 이상일 경우 공유기를 설치한다. 공유기간의 거리가 최소 mid는 만족해야 하기 때문에
            cnt += 1
            s = house[idx]
    return False if cnt < C else True   # 공유기의 설치 개수가 C보다 작으면 mid는 만족하지 않음!

def solution(min_d, max_d):
    while min_d <= max_d :
        mid = (min_d + max_d) // 2

        if check(mid):
            min_d = mid + 1
        else:
            max_d = mid - 1
    return max_d

# run test
import sys
input = sys.stdin.readline  # sys안하고 하면 시간 차이가 많이남
N, C = map(int, input().split(" "))
house = []
for i in range(N):
    house.append(int(input()))
house.sort()
print(solution(1, house[-1] - house[0]))