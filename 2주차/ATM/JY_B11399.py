# baekjoon 11399 : ATM
# solved by JY
# DATE : 2021.01.17
# Greedy 알고리즘

def solution():
    answer, wait = 0, 0
    for i in range(n):
        wait += time[i]
        answer += wait
    return answer

# run test
n, time = int(input()), list(map(int, input().split()))
time.sort()
print(solution())