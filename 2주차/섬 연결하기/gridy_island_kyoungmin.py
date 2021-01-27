# 섬 연결하기

# n<1<100
# cost의 길이는 <=((n-1)*n)/2)
# cost[[]]
# 순서가 바뀌어도 같은 연결이다
# bfs 알고리즘을 이용한다
# stack 이용? min값 찾기
# 연결된 값 중에 가장 최소인 값을 찾는다

# 순서가 바뀌더라도 같은 연결로 봅니다
# 따라서 출발,도착 번호가 방문 배열에 둘 다 함께 있는지를 체크해주어야 한다

# 최소값 문제 -> 정렬을 먼저 생각한다
# 정렬 이후의 상황에 대해서 고민해보기

def solution(n,costs):
    answer=0
    costs.sort(key=lambda x:x[2]) # cost를 기준으로 오름차순으로 정렬
    visited=[costs[0][0]] 
    while len(visited)!=n: # 모든 노드에 방문했을 경우 탈출

        # 정렬 되어있는 상황이므로 costs 배열을 순차적으로 수행하면 된다
        for cost in costs:  # costs 배열에 있는 데이터를 가지고 반복
            if (cost[0] in visited )and (cost[1] in visited): continue # 이미 수행한 노드인지 판단
            if (cost[0] in visited) or (cost[1] in visited): # 해당 노드가 연결되어 있는지 확인
                answer+=cost[2]
                visited.append(cost[0]) 
                visited.append(cost[1]) # 출발,도착 노드를 모두 넣어주고 해당 노드들이 수행된 노드라는 것을 인지시킴
                visited=list(set(visited)) # set 자료형을 이용한 visited 배열의 중복을 제거
                break

    return answer
    

print(solution(4,	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
