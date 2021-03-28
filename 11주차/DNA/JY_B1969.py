# baekjoon 1969 : DNA
# solved by JY
# DATE : 2021.03.25
# Greedy, dictionary 사용

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
DNA = [{} for _ in range(M)]
for _ in range(N):
    tmp = list(input().rstrip('\n'))
    for idx in range(M):
        if tmp[idx] not in DNA[idx]:
            DNA[idx][tmp[idx]] = 1
        else:
            DNA[idx][tmp[idx]] += 1
    
DNA = [sorted(sorted(DNA[m].items()), key=lambda x:x[1], reverse=True) for m in range(M)]

ans, ret = '', 0
for idx in range(M):
    st, cnt = DNA[idx][0]
    ans += st
    ret += N - cnt

print(ans)
print(ret)