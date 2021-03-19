# d[i][0] : i번 노드가 루트인 서브트리에서, i번 노드가 워크숍에 불참하는 경우의 최적해

# d[i][1] : i번 노드가 루트인 서브트리에서, i번 노드가 워크숍에 참석하는 경우의 최적해

# sum_child[i] = sum(min(d[k][0] , d[k][1])) {i의 모든 자식 노드 k에 대해서}
# # 보조 배열 sum_child를 이용
# d[i][1] = sales[i] + sum_child

# i의 모든 자식 노드 k에 대해서, d[k][0] > d[k][1] 를 만족하는 k개가 한 개라도 있다면:
# d[i][0] = sum_child 

# i의 모든 자식 노드 k에 대해서, d[k][0] > d[k][1] 를 만족하는 k개가 한 개도 없다면:
# d[i][0] = sum_child + min(d[k][1] - d[k][0])

# d[k][0] > d[k][1] 를 만족하는 k개가 한 개라도 있다면 

# d[k][0] > d[k][1] 를 만족하는 k개가 한 개도 없다면

tree=[[] for _ in range(300000)]
sum=[0]*300000
dp=[[0,0] for _ in range(300000)]
def go(root, sales): # chile를 찾는 함수
    for child in tree[root]: # tree
        go(child,sales)
    if not tree[root]: # 해당 root에 값이 없을 경우
        dp[root][0]=0 # 0을 넣어준다? 아직은 팀장이 불참하는 경우의 최적해를 구할 수 없으므로 0을 넣어준다
        dp[root][1]=sales[root] # 해당 sales값을 넣어준다
        return
    


    sum=0
    flag=False
    for child in tree[root]:
        sum+=min(dp[child][0],dp[child][1]) # i번 노드가 워크숍에 불참하거나, i번 노드가 워크숍에 참여하는 최소값을 더해준다
        if dp[child][0]>=dp[child][1]: flag=True # 팀장이 불참하는 경우가 더 크면 flag=True

    dp[root][1]=sum+sales[root] # 부모의 sales는 최솟값들의 합과 원래 부모의 sales값

    if flag: # 팀장이 불참하는 경우가 더 큰 경우
        dp[root][0]=sum # 해당 최적해는 sum이 된다
    else: # 팀장이 참여하는 경우가 더 큰 경우
        diff=float('inf') # 무한대
        for child in tree[root]:
            diff=min(diff,dp[child][1]-dp[child][0]) # 최적해를 뺀 것을 할당해준다
        dp[root][0]=sum+diff # 

def solution(sales,links):
    for link in links: 
        tree[link[0]-1].append(link[1]-1)
    go(0,sales)
    return min(dp[0][0],dp[0][1])

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))














# def find(x):
#     if parent[x]==x: # 부모가 자기 자신일 경우
#         return x
#     else:
#         keep_find=find(parent[x])
#         return keep_find
# def union(x,y):
#     root_x=find(x)
#     root_y=find(y)

#     if root_x!=root_y:
#         parent[root_y]=root_x


# def solution(sales, links):
#     answer = 0
#     node=[[] for _ in range(len(sales))]
#     for l in links:
#         node[l[0]-1].append(l[1])
#         node[l[1]-1].append(l[0])
#     print(node) 

#     for i in range(test_cases):
#         parent=dict()
#         number=dict()
#         if x not in parent:
#             parent[x]=x
#             number[x]=1
#         if y not in parent:
#             parent[y]=y
#             number[y]=1
        
#         union(x,y)

    # union-find를 사용해서 푼다?



    # return answer

    # sales는 1번부터 주어진다
    # links는 연결되어 있는 상태를 알려준다

# print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))

