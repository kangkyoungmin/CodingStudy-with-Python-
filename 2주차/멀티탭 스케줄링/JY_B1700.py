# baekjoon 1700 : 멀티탭 스케줄링
# solved by JY
# DATE : 2020.01.17
# Greedy 알고리즘

def solution():
    answer, tab = 0, []
    for i in range(k):
        if use[i] in tab:
            continue
        if len(tab) < n:
            tab.append(use[i])
            continue
        answer += 1
        change, idx = -1, -1
        for j in tab:
            if j not in use[i+1:]:
                change = j
                break
            elif idx < use[i+1:].index(j):
                idx = use[i+1:].index(j)
                change = j            
        tab[tab.index(change)] = use[i]

    return answer

# run test
n, k = map(int, input().split())
use = list(map(int, input().split()))
print(solution())