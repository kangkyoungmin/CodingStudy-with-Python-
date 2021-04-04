# 최소 스패닝 트리
# 모든 정점들을 연결하는 부분 트리 중
# 그 가중치의 합이 최소이다
# = 두 정점이 서로 연결되어 있고 이에 대한 가중치를 최소로 만든다
# 따라서 union-find가 맞다
# 트리 구조라는 것은 사이클이 형성되면 안된다 따라서 사이클의 형성 여부를 검사해준다

parent={} #사전형으로 정의해준다
rank={}
def make_set(a): # parent와 rank를 초기값을 할당해준다
    parent[a]=a

def find(x):
    if parent[x]==x: # 자기자신이 부모가 되면 종료
        return x
    else:
        temp=find(parent[x]) # 재귀함수를 호출해 부모를 찾아낸다 계속
        parent[x]=temp # root값을 갱신해준다 맨 위의 root 꼭대기의 값을 할당받기 위함 이 부분을 수행하지 않으면 parent[y]=x의 형태인데 parent[x]~ 계속 재귀를 불러와서 시간초과가 나옴
        return parent[temp]

# 연결시켜준다
def union(x,y):
    root1=find(x)
    root2=find(y)

    # if root1!=root2: # root가 같으면 뻗어나가는 의미가 없다
    #     # 부모 자식 관계를 만들어준다
    #     parent[root2]=root1
    if root1!=root2:
        parent[root2]=root1

V,E=map(int,input().split())
tree=[]
for _ in range(E):
    i,j,k=map(int,input().split())
    tree.append([i,j,k])
tree.sort(key=lambda x:x[2]) # 최소 신장 트리이기 때문에 weight가 최소인 값부터 할당해준다

# 초기값 할당
for v in range(1,V+1):
    make_set(v)

total=0
cnt=0
for t in tree:
    i,j,weight=t

    if find(i)!=find(j):
        union(i,j)
        total+=weight
        cnt+=1
    if cnt==V-1: # 간선의 개수가 모두 연결되면 종료
        break

print(total)
    







        



