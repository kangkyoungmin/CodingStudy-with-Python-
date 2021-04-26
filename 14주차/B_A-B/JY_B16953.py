# baekjoon 16953 : A->B
# solved by JY
# DATE : 2021.04.14
# DFS 알고리즘 사용

from sys import stdin
input = stdin.readline
A, B = map(int, input().split())
ans = float('inf')
def dfs(num, cnt):
    global ans
    if num <= 0:
        return 
    elif num == A:
        ans = min(ans, cnt)
    elif num % 2 == 0:
        dfs(num//2, cnt + 1)
    elif num % 10 == 1:
        dfs(num//10, cnt + 1)

dfs(B, 1)
print (ans if ans != float('inf') else -1)
