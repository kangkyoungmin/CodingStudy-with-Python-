# 솔루션을 활용한 풀이

def solution(progresses,speeds):
    answer=[]
    time=0
    num=0

    # solution: 
    while len(progresses)>0:
        if progresses[0]+time*speeds[0]>=100: # time이 특정 조건을 만족시킬 때까지 증가 
            progresses.pop(0) # 만족시키면 queue구조와 같이 선출되어 하나씩 빠진다
            speeds.pop(0)
            num+=1 # 이 때 1씩 num이 증가 이 때 time은 그대로이므로 기존 time보다 커질 경우만 else로 이동
        else:
            if num>0: # num이 0보다 크면
                answer.append(num) # 정답배열에 추가시킨다
                num=0 # num을 초기화시키고
                time=0 #time도 초기화시킨다
            else: time+=1 # time의 iterater를 증가시킨다
    answer.append(num)

    return answer

print(solution([93,30,55],[1,30,5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]	))
