# 공유기 설치

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()
left=1
right=arr[-1]-arr[0]

result=0
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
while left<=right:
    mid=(left+right)//2
    old=arr[0] # 현재 집의 위치
    count=1
    
    for i in range(1,n):
        if arr[i]>=old+mid: # gap 상으로 오른쪽에 위치함
            count+=1 # 두 공유기 사이의 거리가 넓다고 간주 count+1
            old=arr[i] 
    if count>=m: # 공유기 수가 더 설치되어야 한다면 간격을 줄인다.
        left=mid+1
        result=mid
    else:
        right=mid-1 # 공유기 수가 더 설치되어야 하므로 간격을 늘려준다

print(result)



