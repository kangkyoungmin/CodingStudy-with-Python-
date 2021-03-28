# baekjoon 2875 : 대회 or 인턴
# solved by JY
# DATE : 2021.03.23
# 구현

import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
ans = M if N//2 >= M else N//2	# 현재 대회에 나갈 수 있는 팀 수
rest = K - ((N+M) - ans*3) if K > ((N+M) - ans*3) else 0	# 대회 팀원 중 인턴에 참가해야 하는 사람 수
ans -= rest//3 if rest%3==0 else rest//3+1	# 인턴 제외 후 대회에 나갈 수 있는 팀 수
print(ans)

