# 방향키는 방향대로 1칸씩
# ctrl+방향키 = 카드가 있는 곳 중 가장 가까운 쪽으로 이동
# enter : 카드 뒤집기
# 숫자가 같으면 같은 것이다
# 무조건 4*4로 고정되어 있다
# 따라서 이는 4*4에 대한 배열을 모두 해보라는 의미
# 방향설정 dir_x, dir_y를 해주고 

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

from collections import deque

def end(e):
    if e.count('0')==16:
        return True
    else:
        return False

def remove_element(b,e): # 뒤집은 것을 제거해주는 함수 prev: 변화시킬 카드 e: 배열
    b=b.replace(e,'0')
    return b
# 이동 조건 (0이 아닌 곳을 찾아서 이동하게 된다)
def move(b,y,x,dy,dx): # e는 전체 배열, x,y는 기존 x,y좌표값, dx,dy는 방향에 따른 좌표값
    nx,ny=x+dx,y+dy # 방향에 따라 더해진다
    # print(b)
    if 0<=nx<4 and 0<=ny<4 and b[ny*4+nx]=="0": #4*4 범위 안에 들어있고 해당 값이 0일 때
        return move(b,ny,nx,dy,dx) # 재귀적으로 이동하게 된다
    else:
        if 0<=nx<4 and 0<=ny<4: # 범위 안에 들어있을 때
            return (ny,nx)
        else: 
            return (y,x)
        
def solution(board, r, c):

    answer = 0
    b='' # 일단 리스트에 있는 것을 문자열로 나타내기
    for i in range(4):
        for j in range(4):
            b+=str(board[i][j])
    q=deque([])

    cnt=0
    enter=-1 # enter를 클릭했던 위치
    q.append((r,c,b,cnt,enter))
    s=set()

    while q:
        y,x,b,c,e=q.popleft()
        pos=4*y+x

        if(y,x,b,e) in s:
            continue
        s.add((y,x,b,e))

        if end(b):
            return c
        
        # 4 일반 방향 이동
        for (dy,dx) in d:
            ny,nx=y+dy,x+dx
            if 0<=ny<4 and 0<=nx<4:
                q.append((ny,nx,b,c+1,e))
        # Ctrl_ 방향 이동
        for (dy,dx) in d:
            ny,nx=move(b,y,x,dy,dx)
            if ny==y and nx==x:
                continue
            q.append((ny,nx,b,c+1,e))
        
        # enter를 하는 경우
        if b[pos]!=0: # 어떤 카드가 들어왔을 때 
            if e==-1: # enter의 초기값
                n_e=pos
                q.append((y,x,b,c+1,n_e))
            else: # 어떤 카드가 이미 하나 뒤집어진 경우
                if e!=pos and b[e]==b[pos]: # e가 뒤집어진 카드 위치와는 같지 않고 해당 카드번호와 같을 때
                    b=remove_element(b,b[e]) # 해당 카드번호에 해당하는 값을 제거해준다
                    q.append((y,x,b,c+1,-1)) # 큐에 해당 enter를 -1로 세팅하고 count+1을 해준다
    return answer







print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))