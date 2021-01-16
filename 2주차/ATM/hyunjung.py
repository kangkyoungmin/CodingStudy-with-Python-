# Baekjoon Online Judge : ATM
# DATE : 2020.01.16
# Greedy 알고리즘


# ATM에서 인출하는데 걸리는 시간이 누적해서 더해짐
# 오름차순으로 정렬해 더함


# 1.
N = int(input())
time = list(map(int, input().split()))
result = 0
time.sort()
for i in range(N):
    for j in range(0,i+1):
        result += time[j]

print(result)


# 2. 
n = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0
for i in range(n):
  result += time[i]*(n-i)
print(result)
