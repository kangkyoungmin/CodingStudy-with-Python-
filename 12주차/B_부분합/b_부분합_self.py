# 부분합 구현문제?
N, S = map(int, input().split())
A = list(map(int, input().split()))

# N: 길이 S: 범위
# sol
# S보다 작으면 계속 더해간다. 그러다가 S보다 커지게 되면 그 이전값부터 다시 시작한다.

hap,left,right,cnt=A[0],0,0,1
result=float('inf')

# 왼쪽에서부터 갯수만큼 left가 돌면 끝
while left<N:
    # 부분합이 S이상이면
    if hap>=S:
        # 최솟값을 넣어준다
        result=min(result,cnt)
    
    # S보다 더 클 때 혹은 right이 정점에 다다르면 left를 전진
    if hap>=S or right == N-1:
        hap-=A[left]
        left+=1
        cnt-=1
    
    # S보다 작을 때 end를 전진
    else:
        right+=1
        cnt+=1
        hap+=A[right]

if result!=float('inf'):
    print(result)
else:
    print(0)

