# 정수 A를 B로 바꾸려고 한다
# 2를 곱한다
# 1을 수의 가장 오른쪽에 추가한다

# A를 B로 바꾸는데 필요한 연산의 최솟값은?

A,B=map(int,input().split())
result=float('inf')
def dfs(num,cnt):
    global result
    if num>B:
        return
    elif num==B:
        result=min(result,cnt)
        return
    else:
        # 자릿수를 판단해준다
        dfs(2*num,cnt+1)
        tmp=str(num)+'1'
        tmp=int(''.join(tmp))
        dfs(tmp,cnt+1)

dfs(A,0)
if result==float('inf'):
    print(-1)
else:
    print(result+1)
