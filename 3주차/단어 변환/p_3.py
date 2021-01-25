# 두 개의 단어 begin,target 단어의 집합 words
# 한 번에 한 개의 알파벳만 바꿀 수 있다
# words에 있는 단어로만 변환할 수 있다

# solution
# 안되면 문구가 나오게 하기 target인 cog는 words 안에 없기 때문에 변환할 수 없습니다.
# 그 다음을 고려한 변환법 (?) nope 일단 경우의 수를 리스트 안에 넣고
# min값을 추려내면 된다!

    
# real=[]
# temp=[]
# def dfs(target,words,answer,v,result):
#     global real
 
#     # global result
#     # global real

#     # v=queue.pop() # v는 string 타입
#     # 다른 게 하나라면
#     if v==target:
#         real.append(answer)
#     for word in words: # 단어들 중에 
#         count=0
#         if word in visited: continue
#         for w in range(len(word)): # 단어들 속 단어를 보면
#             if v[w]!=word[w]: # 해당 단어가 큐 스택 속에 있는 값과 값지 않은 게
#                 count+=1
#         if count==1: # 같지 않은 단어 수가 한 개일 때 
#             for i in range(len(target)):
#                 if word[i]==target[i]:
#                     result.append(i) # 인덱스를 더해준다
#                     temp.append(word)
#             # words.remove(word)  # words에서는 해당 단어 제거
#             dfs(target,words,answer+1,word,result)
#         # dfs처럼 answer개수랑 word, result(인덱스)를 넘겨준다. 탐색 결과 result가 다 차면 return
#             answer+=1
#         if count==0:
#             real.append(answer)
#             break

#         # for i in range(len(target)):
#         #     if v[i]==target[i]:
#         #         result.append(i)
#     if len(target)==len(set(result)):
#         real.append(answer) 


# def bfs(begin,target,words):
#      result=[]
#      dfs(target,words,0,begin,result)   
#      print(min(real))
#      return min(real)


#         # 시작과 타겟을 비교하여 다른 시작에 필요한 타겟 문자들이 있는 데이터들을 큐 스택에 담는다
#         # 관련있는 데이터들을 스택에 담는다
#         # for data in words:
#         #     for i in range(len(target)):
#         #         if begin[i]!=target[i] and data[i]==target[i]: 
#         #             queue.append(data)
    
#             # 현재까지는 큐에 관련 데이터들을 넣었다 이제는 바꿀 차례
#             # 타겟과 특정 문자가 같으면 넘어간다
        

# def solution(begin, target, words):
#     answer = 0

#     answer=bfs("hit","cog",["hot","dot","dog","lot","log","cog"])
#     return answer


    
# print(solution("hit","cog",["hot","dot","dog","lot","log","cog"]))

# answer = 0
def d fs(begin,target,words,visited):
    global answer
    stacks = [begin]
 
    while stacks:
        # 스택을 활용한 dfs 구현
        stack = stacks.pop()
        
        if stack == target:
            return answer
        
        for w in range(0,len(words)):
            # 조건 1. 한 개의 알파벳만 다른 경우
            if len([i for i in range(0,len(words[w])) if words[w][i]!=stack[i]]) == 1:
 
                if visited[w] != 0:
                    continue
 
                visited[w] = 1
 
                # stack에 추가
                stacks.append(words[w])
        
        # depth +
        answer +=1
def solution(begin, target, words):
    global answer
 
    # 조건 2. words에 있는 단어로만 변환할 수 있습니다.
    if target not in words:
        return 0
    
    visited = [0 for i in words]
    
   dfs(begin,target,words,visited)
 
    return answer
 
# 다시 풀어보기



                   


                        
        





