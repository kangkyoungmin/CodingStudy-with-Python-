# 줄 세우기

# M은 키를 비교한 회수이다. 다음 M개의 줄에는
# 키를 비교한 두 학생의 번호 A,B가 주어진다
# 위상 정렬을 이용한다
# 위상 정렬의 핵심: 그래프 형태, 순환이 있는지 여부 확인, weight를 준다
from collections import deque

rank=[] # 순위가 담긴 배열

N,M=map(int,input().split())
connection=[0] *N # 학생들간의 연결 정도를 의미
heights=[[] for _ in range(N)] # 키에 관련되서 자신보다 작은 학생들을 모아 놓은 리스트
for _ in range(M):
    a,b=map(int,input().split()) # 학생들의 키 입력받음
    connection[b-1]+=1
    heights[a-1].append(b)

q=deque()
for i in range(len(connection)):
    if connection[i]==0: # 가장 첫 번째 순서를 큐에 넣어준다
        q.append(i)

while q:
    tmp=q.popleft() # 큐에서 하나를 꺼낸다
    rank.append(tmp+1)

    for j in heights[tmp]:
        connection[j-1]-=1

        if connection[j-1]==0:
            q.append(j-1)

for r in rank:
    print(r,end=' ')


