# 좌표 문제
# (1,1) -> (m,n)
# 오른쪽과 아래쪽으로만 움직인다
# 학교까지 갈 수 있는 최단경로의 개수를 1000000007로 나눈 나머지를 return하도록 함수를 작성
answer = 0
# def solution(m, n, puddles):
#     def dfs(x,y,puddles):
#         global answer
#         if x>m or y>n:
#             return
#         if x==m and y==n:
#             answer+=1
#             return
#         if [x,y] in puddles:
#             return
#         dfs(x+1,y,puddles)
#         dfs(x,y+1,puddles)

#     dfs(1,1,puddles)
#     return answer%1000000007

# print(solution(4,3,[[2,2]]))

def solution(m,n,puddles):
    # solution
    # 만약에 목적지에 도착하면 어떤 set 배열 안에 넣어준다. 
    # 중복을 제거하고
    land=[[0 for a in range(m+1)] for b in range(n+1)]
    land[1][1]=1
    print(land)
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            if [j,i] not in puddles:
                land[i][j]=land[i-1][j]+land[i][j-1]
    return land[n][m]%1000000007

print(solution(4,3,[[2,2]]))
            







    
    
