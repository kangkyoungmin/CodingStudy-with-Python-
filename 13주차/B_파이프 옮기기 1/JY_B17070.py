# baekjoon 17070 : 파이프 옮기기 1
# solved by JY + hint
# DATE : 2021.04.10
# 재귀 알고리즘 사용, pypy3으로 채점 필수
# r < N, c < N 확인된 사항 if 문에서 또 확인하면 시간초과 발생

from sys import stdin
input = stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
def rec(r, c, d):
    if r == N-1 and c == N-1:
        global ans
        ans += 1
        return

    if d == 0:      # 가로
        if c + 1 < N and board[r][c+1] == 0:
            rec(r, c+1, 0)
        if r + 1 < N and c + 1 < N and board[r][c+1] == 0 and board[r+1][c] == 0 and board[r+1][c+1] == 0:
            rec(r+1, c+1, 2)
    elif d == 1:    # 세로
        if r + 1 < N and board[r+1][c] == 0:
            rec(r+1, c, 1)
        if r + 1 < N and c + 1 < N and board[r][c+1] == 0 and board[r+1][c] == 0 and board[r+1][c+1] == 0:
            rec(r+1, c+1, 2)
    else:           # 대각선
        if c + 1 < N and board[r][c+1] == 0:
            rec(r, c+1, 0)
        if r + 1 < N and board[r+1][c] == 0:
            rec(r+1, c, 1)
        if r + 1 < N and c + 1 < N and board[r][c+1] == 0 and board[r+1][c] == 0 and board[r+1][c+1] == 0:
            rec(r+1, c+1, 2)
    
rec(0,1,0)
print(ans)