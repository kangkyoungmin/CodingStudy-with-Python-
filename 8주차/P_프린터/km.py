# 다른 방법으로 다시 도전해보기

# 같은 경우를 체크할 때는 해당 인덱스 뒤에 동일한 값이 있는지를 확인하고
# 없을 때에만 
def solution(priorities, location):
    priorities_cp=priorities[:] # deep copy 해준다
    result=[0] *len(priorities) # result라는 배열을 하나 만들어준다
    i=0
    n=1
    priorities.sort(reverse=True) # priorities를 sort

    while len(priorities)>0: # priorities 만큼 iteration
        if priorities[0]==priorities_cp[i]: #max값과 비교하여 index를 알아낸다
            result[i]=n # 인덱스에 해당되는 result에 값을 집어넣는다
            n+=1 # n을 1씩 증가시킨다
            priorities.pop(0) # 하나를 제거한다
        if i==len(priorities_cp)-1:
            i=0
        else: i+=1              
    return result[location]
    
print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))

