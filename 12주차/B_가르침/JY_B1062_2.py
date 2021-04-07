# baekjoon 1062 : 가르침
# solved by JY
# DATE : 2021.04.01
# 재귀 이용

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
lang = [[] for _ in range(N)]
dic, check, ans = {}, set(), 0

for idx in range(N):
    lang[idx] = set(input().rstrip()) - set('antic')
    check.update(lang[idx])

check = list(check)

for c in check:
    dic[c] = 0

ans = 0
def rec(idx, cnt):
    if cnt == K - 5 or cnt == len(dic):
        global ans
        tmp = {d for d in dic if dic[d] == 1}
        count = 0
        for l in lang:
            if len(l - tmp) == 0:
                count += 1
        
        ans = max(ans, count)
        
    else:
        for i in range(idx, len(check)):
            if dic[check[i]] == 0:
                dic[check[i]] = 1
                rec(i + 1, cnt + 1)
                dic[check[i]] = 0

if K >= 5:
    rec(0, 0)
print(ans)
