# 수 찾기

# M개의 줄에 답을 출력
# 존재하면 1을 존재하지 않으면 0을 출력

# 이분법을 적용하여 풀이

n=int(input())

arr=list(map(int,input().split()))
arr.sort()
m=int(input())
check=list(map(int,input().split()))


for i in range(len(check)):
    ok=0
    left=0
    right=len(arr)-1
    while True:
        if left>right:
            print(0)
            break
        mid=(left+right)//2
        if arr[mid]==check[i]:
            print(1)
            break
        elif arr[mid]>check[i]:
            right=mid-1
        else:
            left=mid+1

# for i in range(len(check)):
#     if check[i] in arr:
#         print(1)
#     else: print(0)


