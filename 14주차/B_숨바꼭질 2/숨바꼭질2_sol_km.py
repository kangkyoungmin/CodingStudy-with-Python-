from collections import deque
# 숨바꼭질 bfs 이용
N,K=map(int,input().split()) # 수빈이, 동생
ch=[[-1,0] for _ in range(100001)]

# 수빈이가 동생을 찾는 가장 빠른 시간
# 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수

def bfs(n):
    de=deque()
    de.append(n)
    ch[n][0]=0 # 가장 빠른 시간
    ch[n][1]=1 # 방법의 수

    while de:
        x=de.popleft()

        for i in (x+1,x-1,x*2): # 최소의 조건이 되려면 세 가지 경우의 수 중 하나를 고른다
            if 0<=i<100001: 
                if ch[i][0]==-1: #처음 들르는 경우
                    ch[i][0]=ch[x][0]+1 # 시간을 1 증가시킨다
                    ch[i][1]=ch[x][1] # 방법의 개수
                    de.append(i)
                elif ch[i][0]==ch[x][0]+1: # 한번 이상 들르는 경우
                    ch[i][1]+=ch[x][1] # 방법 더하기

ch=[[-1,0] for _ in range(100001)]
bfs(N)
print(ch[K][0])
print(ch[K][1])
print(ch)
                    
