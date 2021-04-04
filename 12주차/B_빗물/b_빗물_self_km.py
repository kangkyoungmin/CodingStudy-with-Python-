# 빗물이 채워지는 조건: 자신보다 같거나 더 낮은 높이를 지니고 있으면 채워진다. 
# 아니면 채워지지 않는다

# solution
# 기준을 세우고 기준보다 더 큰 것을 왼쪽에서 찾는다
# 기준보다 더 큰 것을 오른쪽에서 찾는다

n,m=map(int,input().split())

block=list(map(int,input().split()))

# 오른쪽으로 가면서 자신보다 크거나 같은 블록을 찾는 함수
def find_block(x): # 변수 x: 채워져 있는 블록의 개수
    max_block=[0,0] # 첫 번째 인덱스는 인덱스 두 번째 인덱스는 높이
    for i in range(x+1,m):
        if block[i]>=block[x]: # 자신보다 큰 게 있으면 바로 해당 인덱스를 리턴해준다
            return i
        if max_block[1]<=block[i]: # 자신보다 크지 않을 경우에는 작은 것 중 가장 큰 것을 알아낸다
            max_block[1]=block[i]
            max_block[0]=i
    return max_block[0]

def count(x,y):
    # 자신보다 같거나 큰 놈이 있으면 해당하는 만큼 정답에 더해준다. 
    # 자신보다 같거나 크지 않으면 자신의 높이만큼 비를 채워준다
    rain_water=min(block[x],block[y])
    temp=0
    for j in range(x+1,y):
        temp+=rain_water-block[j] # 차만큼을 temp에 더해준다
        block[j]=rain_water # 비가 와서 차오른 만큼의 높이로 갱신해준다
    return temp

i=0
result=0
while i<m-1: # 모든 가로의 길이만큼 반복해준다
    tmp=find_block(i) # block을 찾고
    result+=count(i,tmp)  # 찾은 블락까지 사용된 빗물들을 정답에 더해준다
    i=tmp # 인덱스 값 갱신

print(result)
     

