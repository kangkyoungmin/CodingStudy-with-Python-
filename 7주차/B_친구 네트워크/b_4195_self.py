# 친구의 네트워크
# union-find algorithm을 이용한 풀이
# union 함수를 통해 parent 노드를 만들어준다
# fine 함수를 통해 parent 노드를 찾아준다
# test 케이스에서는 parent인지 아닌지를 확인해준다

def find(x):
    if parent[x]==x:
        return x
    else: # parent가 자기 자신이 아닐 경우
        root_x=find(parent[x]) # x의 root값
        parent[x]=root_x # x의 parent를 x의 root값으로 할당한다
        return parent[x] # x의 parent값을 반환해준다

# x와 y의 parent값이 같을 경우 넘긴다
# x와 y의 parent값이 다를 경우 y의 root 노드로 x값을 지정해준다
def union(x,y):
    root_x=find(x) # x의 root 노드를 찾아준다
    root_y=find(y) # y의 root 노드를 찾아준다

    if root_x!=root_y: 
        parent[root_y]=root_x
        number[root_x]+=number[root_y] #number[root_x] 값을 key로 하여 number[root_y]가 value가 되게 한다

test_cases=int(input())   
    

for i in range(test_cases):
    parent=dict()
    number=dict()
    a=int(input())
    for j in range(a):
        x,y=input().split(" ")

        if x not in parent:
            parent[x]=x
            number[x]=1
        if y not in parent:
            parent[y]=y
            number[y]=1
    
        union(x,y)
        print(number[find(x)]) # 이렇게 하면 fine(x)를 통해 root를 찾고 root에 해당하는 number 배열에 관한
        # 노드들이 쭉 딸려나오게 된다






