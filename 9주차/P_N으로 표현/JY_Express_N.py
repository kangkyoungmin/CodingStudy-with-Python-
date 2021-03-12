# programmers L3 : N으로 표현
# solved by JY
# DATE : 2021.03.11
# DP 사용
# dp[i] = N을 i+1번 사용했을 때 나올 수 있는 수의 집합(idx 0부터 시작)
# ex) dp[3] = tmp + { dp[0]~dp[2] } + { dp[1]~dp[1] } + { dp[2]~dp[0] }
# tmp = NNNN
# ~ = 사칙연산(+, -, *, //)

def solution(N, number):
    if number == N:
        return 1
    dp = [set() for _ in range(8)]
    dp[0] = {N}
    dp[1] = {N*10+N, N+N, N-N, N*N, N//N}
    if number in dp[1]:
        return 2
    
    tmp = N*10+N
    for i in range(2,8):
        tmp = tmp*10 + N
        dp[i].add(tmp)
        for j in range(i):
            for one in dp[j]:
                for two in dp[i-j-1]:
                    dp[i].add(one + two)
                    dp[i].add(one - two)
                    dp[i].add(one * two)
                    if two != 0:
                        dp[i].add(one // two)
        if number in dp[i]:
            return i+1
    return -1

# run test
print(solution(5, 12), 4)
print(solution(2, 11), 3)