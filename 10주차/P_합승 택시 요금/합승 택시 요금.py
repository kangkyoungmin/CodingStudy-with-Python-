# n: 지점 갯수
# s,a,b: 지점
# 기존의 플로이드-워셜 알고리즘은 최단 거리에 대한 정보를 기록하고 출력하는 쪽
# 여기서는  

def solution(n, s, a, b, fares):
    answer = 0

    # 플로이드 워셜 알고리즘 vs 다익스트라 알고리즘
    # a에서 b로 가는데 s를 거쳐서 가는 최단 거리?
    # s에서 a로 가는 최단 거리, s에서 b로 가는 최단 거리
    # 넘겨줄 때 노드까지 같이 넘겨준다?
    # 
    # distance를 배열로 할당
    distance=[[float('inf')]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x==y:
                distance[x][y]=0

    for k in fares:
        for i in range(n): # 출발 노드
            if k[0]!=i+1:
                continue
            for j in range(n): # 도착 노드
                if k[1]!=j+1:
                    continue
                # if i==j: 
                #     distance[i][j]=0
            # if k[0]==i+1 and k[1]==j+1:
                distance[i][j]=k[2]
                distance[j][i]=k[2]
    # print(distance)
    # i=s
    # S에서 A, S에서 B
    answer=[]
 
    for k in range(0,n): # 거치는 점
        for i in range(0,n): #출발점
            for j in range(0,n): #도착점
                # if distance[s-1][a-1]>distance[s-1][k]+distance[k][a-1]:
                #     x.append(k)
                # if distance[s-1][b-1]>distance[s-1][k]+distance[k][b-1]:
                #     y.append(k)
                if distance[i][j]>distance[i][k]+distance[k][j]:
                    distance[i][j]=distance[i][k]+distance[k][j]
                
    # 출발점에서 특정 지점을 거쳐서 가는 경우 어떤 점을 거치는 것이 가장 좋은지를 설정
    for k in range(0,n):
        answer.append(distance[s-1][k]+distance[k][a-1]+distance[k][b-1])

    return min(answer)
                

                   

    # print(distance)


    # for a in range(0,n):
    #     for b in range(0,n):
    #         if distance[a][b]!=float('inf'):
    #             print(distance[a][b])




print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

