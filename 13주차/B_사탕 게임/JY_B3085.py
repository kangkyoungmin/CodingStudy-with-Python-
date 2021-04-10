# baekjoon 3085 : 사탕 게임
# solved by JY
# DATE : 2021.04.08
# BruteForce 알고리즘
# 처음 allcheck() 한 번 하고 이후 swap시 해당 행,열만 확인

import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(str, input().strip())) for _ in range(N)]

def allcheck(): # 모든 board 확인하는 함수
    cnt = 1
    for i in range(N):
        rtmp, ctmp = 1, 1
        for j in range(N-1):
            rtmp = rtmp + 1 if board[i][j] == board[i][j+1] else 1
            ctmp = ctmp + 1 if board[j][i] == board[j+1][i] else 1
            cnt = max(cnt, rtmp, ctmp)
    return cnt

def line(rc, k):    # 한 줄만 확인하는 함수
    ret, cnt = 1, 1
    if k == 0:      # rc 행
        for i in range(N-1):
            cnt = cnt + 1 if board[rc][i] == board[rc][i+1] else 1
            ret = max(ret, cnt)
    else:           # rc 열
        for i in range(N-1):
            cnt = cnt + 1 if board[i][rc] == board[i+1][rc] else 1
            ret = max(ret, cnt)
    return ret
        
def check(r,c,nr,nc):
    return max(line(r, 0), line(nr, 0), line(c, 1), line(nc, 1))

def swap(r, c, nr, nc):
    tmp = board[r][c]
    board[r][c] = board[nr][nc]
    board[nr][nc] = tmp

ans = allcheck()
for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:
            swap(i, j, i, j+1)  # 행
            ans = max(ans, check(i, j, i, j+1))
            swap(i, j, i, j+1)
        if board[j][i] != board[j+1][i]:
            swap(j, i, j+1, i)  # 열
            ans = max(ans, check(j, i, j+1, i))
            swap(j, i, j+1, i)
print(ans)