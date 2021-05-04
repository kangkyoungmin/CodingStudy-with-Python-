import sys
from collections import deque
n,s,m=map(int,sys.stdin.readline().split())
dp=[0]*(m+1)
# n개의 곡을 연주
song=list(map(int,input().split()))

result=[[0]*(m+1) for _ in range(n+1)]

result[0][s]=1

for i in range(1,n+1):
    for j in range(m+1):
        if result[i-1][j]==0:
            continue
        if j+song[i-1]<=m:
            result[i][j+song[i-1]]=1
        if j-song[i-1]>=0:
            result[i][j-song[i-1]]=1

check=False
for k in range(m,-1,-1):
    if result[-1][k]==1:
        print(k)
        check=True
        break
if not check:
    print(-1)



            