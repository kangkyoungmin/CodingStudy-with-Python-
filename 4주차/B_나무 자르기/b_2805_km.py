# 나무 자르기

# 나무 M미터가 필요
# M의 범위를 보고 판단을 하면 된다

n,m=map(int,input().split())

tree=list(map(int,input().split()))

start=0
end=max(tree)

ans=0
while start<=end:
    mid=(start+end)//2
    temp=0

    for t in tree:
        if t-mid>0:
            temp+=(t-mid)
    
    if temp>=m:
        ans=mid
        start=mid+1
    else: 
        end=mid-1
print(ans)

