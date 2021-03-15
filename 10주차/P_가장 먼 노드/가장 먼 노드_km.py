# solution
# 1. 각 노드당 연결되어 있는 노드들을 리스트로 표현해준다
# 2. deque를 이용하여 1번 노드에서 빼내어 가장 멀리 떨어진 노드들을 찾고
# 3. 뺴낼 때마다 count를 세준다

from collections import deque
def solution(n, edge):
    # 먼저 인덱스마다 1부터 n까지 edge에서 연결된 것을 할당해준다
    # depth에 대한 문제
    # num[depth]와 같이 해당 인덱스에 depth 넘버를 기재
    # num[i]=depth?
    # 다음 노드가 있으면 depth를 증가시킨다?
    # depth를 재귀함수와 같이 queue안에 함께 넘겨주는 방식으로 진행한다
    node=[[] for _ in range(n+1)]
    num=[0]*(n+1)
    for e in edge:
        node[e[0]].append(e[1])
        node[e[1]].append(e[0])

    def bfs(node,edge):
        queue=deque([[1,0]]) # index,depth
        visited=[0]*(n+1)
        visited[1]=1

        while queue:
            index,depth=queue.popleft()
            
            num[index]=depth
            for t in node[index]: 
                # if t in visited: # t를 이미 방문한 경우
                #     continue
                if visited[t]==1:
                    continue
                # visited.append(t)
                visited[t]=1
                queue.append([t,depth+1])
                    
        return num.count(max(num))
    answer=bfs(node,edge)
    return answer
        

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

# 이 문제의 쟁점: 
# bfs 알고리즘에 대한 확실한 이해
# visited 배열 만들 때 단순히 문자 그대로를 넣기보다는 int 개념으로 만들어놓고
# 비교하는 것이 훨씬 시간 복잡도가 빠르다
# bfs 알고리즘 통해서 데이터를 넘길 때 depth를 큐 안에 함꼐 넣어주는 방식(재귀와 유사 방식)