# baekjoon 2252 : 줄 세우기
# solved by JY
# DATE : 2021.04.05
# 위상정렬

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
back = [[] for _ in range(n+1)]    # 내 뒤에 오는 학생들
cnt = [0]*(n+1)     # 나보다 앞에 있어야 하는 학생 수
for idx in range(m):
    f, b = map(int, input().split())
    back[f].append(b)
    cnt[b] += 1

que, ans = [], []
for idx in range(1, n+1):
    if cnt[idx] == 0:
        que.append(idx)

while que:
    p = que.pop(0)
    ans.append(p)

    for b in back[p]:
        cnt[b] -= 1
        if cnt[b] == 0:
            que.append(b)

print(' '.join(map(str,ans)))