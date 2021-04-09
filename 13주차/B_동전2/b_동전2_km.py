import sys
r = sys.stdin.readline

N, K = map(int, r().split())
coins = sorted([int(r()) for _ in range(N)])

arr = [10001] * (K+1) # 초기값으로 최대값으로 설정해준다 
arr[0] = 0

for i in range(N):
    for j in range(coins[i], K+1): # 코인을 하나씩 받는다
        arr[j] = min(arr[j], arr[j-coins[i]] + 1) # 최솟값에서 하나씩 더해준다

arr[-1] = arr[-1] if arr[-1] != 10001 else -1
print(arr[-1])