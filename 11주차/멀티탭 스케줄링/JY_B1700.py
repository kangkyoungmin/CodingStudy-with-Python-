# baekjoon 1700 : 멀티탭 스케줄링
# solved twice by JY 
# DATE : 2021.03.25
# Greedy

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
use = list(map(int, input().split()))
multitap = [-1]*N
ans = 0
for idx in range(K):
    if use[idx] in multitap:    # 이미 꽂혀있음
        continue
    if -1 in multitap:          # 빈 자리 있음
        multitap[multitap.index(-1)] = use[idx]
    else:   # 빈 자리 없음
        flag = False
        # 더 이상 사용하지 않는 용품 제거
        for midx in range(N):
            if multitap[midx] not in use[idx:]:
                multitap[midx] = use[idx]
                ans += 1
                flag = True
                break

        # 꽂혀있는 용품들 중 가장 나중에 사용하는 용품 제거
        if not flag:
            cnt = [0]*N
            for uidx in range(idx, K):
                if use[uidx] in multitap:
                    cnt[multitap.index(use[uidx])] = 1
                
                if sum(cnt) == N:
                    multitap[multitap.index(use[uidx])] = use[idx]
                    ans += 1
                    break

print(ans)
