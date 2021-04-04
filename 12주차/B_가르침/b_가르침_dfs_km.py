# 가르침

# 모든 단어는 중복되지 않는다
def dfs(x,y): # x는 count
    global result
    if y==m-5: # 개수가 지정된 것보다 지나치면 return
        cnt=0
        for word in words:
            check=0
            for w in word:
                if not learn[ord(w)-ord('a')]:
                    check=1
                    break
            if check==0:
                cnt+=1
        if result<cnt:
            result=cnt
            return
    
    # 랜덤하게 문자를 재귀함수를 통해 탐색한다
    for i in range(x,26):
        if not learn[i]: 
            learn[i]=True
            dfs(i,y+1)
            learn[i]=False #learn은 쭉 재귀동안 공유된다 그리고 False로 지정함으로써 



n,m=map(int,input().split())

words=[]
for _ in range(n):
    words.append(set(input()).difference('a','n','t','i','c'))

# print(words)
learn=[False]*26

# learn에 대한 것: learn이 이미 True인 것이 있고 True인 것이 m-5일 떄 
for c in ['a','n','t','i','c']:
    learn[ord(c)-ord('a')]=True # 5개에 대해서는 True로 지정해준다

result=0
dfs(0,0) 

if m<5:
    print(0)
else:
    print(result)



