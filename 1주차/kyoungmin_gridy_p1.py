# from collections import deque
# # 입력값
# n=int(input())
# lost=list(map(int,input().split(",")))
# reserve=list(map(int,input().split(",")))

# # lost를 담을 queue 생성
# queue=deque()
# for i in range(len(lost)):
#     queue.append(lost[i])

# answer=n-len(lost)
# if queue:
#     for i in range(len(lost)):
#         num=queue.popleft()
#         for j in range(len(reserve)):
#             if num==reserve[j]-1 or num==reserve[j]+1:
#                 answer+=1
#                 reserve[j]=-1
#                 break
# else:
#     print(answer)


# print(answer)

# 앞번호나 뒷번호 학생들에게 체육복을 빌려줄 수 있다
# 전체 학생의 수 : n, 체육복을 도난당한 학생들의 번호의 배열 :lost
# 여벌의 체육복을 가져온 학생들의 배열: reverse
# 출력값: 체육수업을 들을 수 있는 학생의 최댓값

#솔루션 : 
# 만약 lost 배열의 리스트 내 값의 +1,-1의 값이 reverse 배열에서 동일한 값이 있으면
# lost배열의 해당 값이 pop되고, count가 1 증가한다 (deque 사용)
# 기본적인 count값은 reverse 배열의 길이와 동일하다
    
# from collections import deque

# def solution(n, lost, reserve):
    
    # 입력값
    # n=int(input())
    # lost=list(map(int,input().split(",")))
    # reserve=list(map(int,input().split(",")))

    # lost를 담을 queue 생성
    # queue=deque()
    # for i in range(len(lost)):
    #     queue.append(lost[i])

    # answer=n-len(lost)
    # # 만약 큐가 비어있지 않다면
    # if queue:
    #     for i in range(len(lost)):
    #         num=queue.popleft()
    #         for j in range(len(reserve)):
    #             if num==reserve[j]-1 or num==reserve[j]+1:
    #                 answer+=1
    #                 reserve[j]=-1
    #                 break
    # # 큐가 비어있다면
    # else:
    #     return answer


    # return answer

# 앞번호나 뒷번호 학생들에게 체육복을 빌려줄 수 있다
# 전체 학생의 수 : n, 체육복을 도난당한 학생들의 번호의 배열 :lost
# 여벌의 체육복을 가져온 학생들의 배열: reverse
# 출력값: 체육수업을 들을 수 있는 학생의 최댓값

#솔루션 : 
# 만약 lost 배열의 리스트 내 값의 +1,-1의 값이 reverse 배열에서 동일한 값이 있으면
# lost배열의 해당 값이 pop되고, count가 1 증가한다
# 기본적인 count값은 reverse 배열의 길이와 동일하다
    
# from collections import deque

def solution(n, lost, reserve):
    
    # 중복 제거
    # 집합 자료형으로 set_reserve와 set_lost가 중복되는 것을
    # 차집합을 통하여 방지한다
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)
    
    # 체육복이 남는 학생들을 대상으로
    for i in set_reserve:
        # 빌려줄 수 있는 번호에 해당하는 번호가 lost 배열에 있을 경우
        # 이 때 작은 숫자부터 빌려줄 수 있도록 한다
        if i-1 in set_lost:
            set_lost.remove(i-1)
            
        elif i+1 in set_lost:
            set_lost.remove(i+1)
            
    return n-len(set_lost)

print(solution(5,[2,4],[1,3,5]))