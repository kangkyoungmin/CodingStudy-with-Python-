# 네트워크 
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 배열 computers가 매개변수로 주어짐
# 네트워크의 개수를 return 하도록 solution 함수 작성
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]=1

def solution(n,computers):
    dfs(n,computers,0,0)
    return cnt

stack=[]
cnt=1
# idx: 타 네트워크와의 연결 확인 i : 각 네트워크들
def dfs(n,computers,idx,check):
    global stack
    global cnt

    if idx>len(computers)-1:
        return
    
    for i in range(n):
        # if i==idx: continue
        if (idx in stack) and (i in stack):
            continue
        if computers[idx][i]==1:
            stack.append(i)
            if idx!=i:
                dfs(n,computers,i,check)
    # 현재의 idx가 아니면 다른 재귀함수들은 return 시킨다
    if check!=idx: return
    # 스택에 모든 컴퓨터 number가 들어있으면 리턴
    if n==len(set(stack)):
        return
    # 아니면 count한다
    else:
        cnt+=1
    # 스택 안에 없는 것에 대한 재귀함수를 실행시킨다
    while idx<n:
        idx+=1
        check+=1
        if (idx<n) and (idx not in stack):
            dfs(n,computers,idx,check)

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))




# 너비 우선 탐색을 해야한다
# 큐를 이용한 탐색
# 방문 정보를 넣고, 1이면 쭉 탐색되고 0을 만나면 stop, 나머지를 쭉 탐색하다가 
# 재귀함수를 이용하여 idx값이 0인 것부터 탐색을 들어간다. 첫 번째 리스트에서 1인 것이 있으면
# 해당 인덱스의 computer에 들어가서 다른 1인 것을 탐색하고 
# 만약 인덱스 범위를 초과(computer배열)하면 stop, 자기 자신의 인덱스 제외
# 스택에서 만약 출발지,도착지의 컴퓨터 모두 존재하면 같은 네트워크이므로 패스

