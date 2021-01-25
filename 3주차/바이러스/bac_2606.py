# 바이러스

# 연결되어 있으면 바이러스에 걸리고 
# 연결되어 있지 않으면 바이러스에 걸리지 않는다
# 너비 우선 탐색 문제?


# from collections import defaultdict

# 컴퓨터의 수
n=int(input())
m=int(input())

connect=[]
for i in range(m):
    connect.append(list(map(int,input().split())))

# for key,value in connect:  # key값당 value들이 network에 저장된다
#     network[key].append(value)


# visited=[]
def dfs(key,connect):
    visited=[]
    count=0
    i=0

    queue=[key]
    visited=[key]
    # for idx,data in enumerate(network[key]): #1기준 2,5
    #     f=network[key].pop(idx)
    while queue:
        v=queue.pop()
    
        for i in range(len(connect)):
            if (v==connect[i][0]) and (connect[i][1] not in visited):
                queue.append(connect[i][1])
                visited.append(connect[i][1])
                count+=1
    return len(visited)-1

print(dfs(1,connect))




