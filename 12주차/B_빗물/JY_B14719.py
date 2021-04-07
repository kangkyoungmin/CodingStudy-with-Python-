# baekjoon 14719 : 빗물
# solved by JY
# DATE : 2021.03.31
# 구현
# 아래부터 위로 W 돌면서 빈공간 확인

import sys
input = sys.stdin.readline
H, W = map(int, input().split())
height = list(map(int, input().split()))
ans = 0
for h in range(1, H + 1):
    sflag = False   # 왼쪽에서 처음 나타나는 블록 확인
    tmp = 0
    for w in range(W):
        if not sflag and height[w] >= h:
            sflag = True
            continue
        if sflag:
            if height[w] < h:
                tmp += 1
            else:
                ans += tmp
                tmp = 0

print(ans)