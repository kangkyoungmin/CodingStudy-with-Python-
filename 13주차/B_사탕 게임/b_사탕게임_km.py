# 사탕의 개수
from collections import Counter
n=int(input())

candy=[]
for _ in range(n):
    candy.append(list(input()))
tmp=0 # 결과를 담을 변수

#width 같은 행끼리만 바꾸는 경우
def width():
    global tmp
    for i in range(0,n):
        cnt=1
        for j in range(1,n):
            if candy[i][j]==candy[i][j-1]: # 연속적으로 같은 경우
                cnt+=1
            else: # 연속적으로 같지 않을 때
                if tmp<cnt: # 
                    tmp=cnt
                cnt=1
        if tmp<cnt: # 행 모두 같을 경우
            tmp=cnt

def height():
    global tmp
    for i in range(0,n):
        cnt=1
        for j in range(1,n):
            if candy[j][i]==candy[j-1][i]:
                cnt+=1
            else: 
                if tmp<cnt:
                    tmp=cnt
                cnt=1
        if tmp<cnt:
            tmp=cnt

for i in range(0,n):
    for j in range(1,n):
        candy[i][j],candy[i][j-1]=candy[i][j-1],candy[i][j]
        width()
        height()
        candy[i][j-1],candy[i][j]=candy[i][j],candy[i][j-1]

for j in range(n):
    for i in range(1,n):
        candy[i][j],candy[i-1][j]=candy[i-1][j],candy[i][j]
        width()
        height()
        candy[i-1][j],candy[i][j]=candy[i][j],candy[i-1][j]
print(tmp)





