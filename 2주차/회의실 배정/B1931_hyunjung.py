# Baekjoon Online Judge : 회의실배정
# DATE : 2020.01.17
# Greedy 알고리즘


# 끝나는 시간을 기준으로 정렬 -> 시작 시간을 기준으로 정렬
#  ex 2 / (2,2) (1,2) 있을때 첫번째 기준으로 회의실배정:1개의 방 /두번째 : 2개의 방
# 첫번째 회의 끝나는 시간 기준으로 다음 회의 시작시간 찾음
# 회의 끝나는 시간 초기화

N = int(input())
times = [list(map(int, input().split())) for i in range(N)]
times.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간으로 우선 정렬, 시간 같을경우 시작시간으로 정렬
end = times[0][1]
meeting = 1

for time in times[1:]:
    if end <= time[0]:
        end = time[1]
        meeting += 1

print(meeting)


# 시간이 오래 걸림
# 시간 줄일 수 있는 방법 생각



# 다중배열 정렬
# 1. 첫번째 key값을 기준으로 정렬
# time.sort(key=lambda x:x[0])
# 2. 두번째 key값을 기준으로 정렬
# time.sort(key=lambda x:x[1])
# 3. 두번째 key값 -> 첫번째 key값 기준 정렬
# time.sort(key=lambda x:(x[1],x[0]))

# 파이썬 입력 빠르게
# import sys
# a = sys.stdin.readline().rstrip()
