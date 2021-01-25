# n개의 수가 있는데 
# 이를 적절히 더하거나 빼서 타겟 넘버를 만들려고 한다
# 사용할 수 있는 숫자가 담긴 배열: numbers
# 타겟 넘버 target이 매개변수로 주어짐 
# 숫자를 적절히 더하고 뺴서 타겟 넘버를 만드는 방법의 수를 return

# solution
# 깊이 우선 탐색을 수행하면 된다

# 재귀함수를 통하여 +,-인 경우에 대한 경우의 수로 탐색을 들어간다
# 타겟값과 일치하게 되면 count++, 
# 재귀의 break 조건: true,false의 인덱스가 5이면 멈춘다

answer=0
def bfs(numbers,target,idx,cnt):
    global answer
    if idx==len(numbers):
        if cnt==target:
            answer+=1
    if idx>len(numbers)-1:
        return
        
    
    bfs(numbers,target,idx+1,cnt+numbers[idx])
    bfs(numbers,target,idx+1,cnt-numbers[idx])

    return answer


def solution(numbers,target):
    answer=0
    answer=bfs(numbers,target,0,0)
    return answer

print(solution([1,1,1,1,1],3))
