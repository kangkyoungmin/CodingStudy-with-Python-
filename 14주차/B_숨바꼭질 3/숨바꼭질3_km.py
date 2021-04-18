# 수빈이는 동생과 숨바꼭질을 하고 있다
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오
# bfs를 활용한다
from collections import deque
n,k=map(int,input().split()) # 입력

# 풀이 방법
# weight가 다르므로
# 순간이동할 경우 q의 왼쪽에 넣어주고 순간이동이 아닌경우 q의 오른쪽에 넣어준다

check=[False]*100001

def bfs(x):
    q=deque()
    q.append(x)
    check[x]=True

    while q:
        de=q.popleft()

        for i in (de*2,de+1,de-1):
            if 0<=i<=100000: # 범위 안에 있을 때만
                if i==de*2 and not check[i]: # 순간이동할 경우
                    ch[i]=ch[de]
                    check[i]=True
                    q.appendleft(i)
                elif i==de+1 and not check[i]:
                    ch[i]=ch[de]+1 # time+1
                    check[i]=True
                    q.append(i)
                elif i==de-1 and not check[i]:
                    ch[i]=ch[de]+1 # time+1
                    check[i]=True
                    q.append(i)


ch=[0]*100001 # 10만 개의 배열을 만드는데, time에 대한 배열만 
# for i in range(n,100001):
#     if i%n==0:
#         ch[i]=0

bfs(n)
print(ch[k])
                

