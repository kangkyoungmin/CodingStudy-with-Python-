# 앞번호나 뒷번호 학생들에게 체육복을 빌려줄 수 있다
# 전체 학생의 수 : n, 체육복을 도난당한 학생들의 번호의 배열 :lost
# 여벌의 체육복을 가져온 학생들의 배열: reverse
# 출력값: 체육수업을 들을 수 있는 학생의 최댓값

#솔루션 : 
# 만약 lost 배열의 리스트 내 값의 +1,-1의 값이 reverse 배열에서 동일한 값이 있으면
# lost배열의 해당 값이 remove된다
# n에서 lost배열의 길이만큼을 빼면 정답이 된다

# def solution(n, lost, reserve):
    
#     # 중복 제거(예외 케이스 제외)
#     set_reserve=set(reserve)-set(lost)
#     set_lost=set(lost)-set(reserve)
    
#     for i in set_reserve:
#         if i-1 in set_lost:
#             set_lost.remove(i-1)
            
#         elif i+1 in set_lost:
#             set_lost.remove(i+1)     
#     return n-len(set_lost)

# def solution(name):
#     answer = 0
#     loc=[]
#     # A가 아닌 인덱스 위치를 loc 배열에 추가한다
#     for k in name:
#         if k!='A' and k!=name[0]:
#             loc.append(name.index(k))
    
#     for i in name:
#         # 위,아래 결정
#         if ord(i)-65<ord('Z')-ord(i)+1:
#             answer+=ord(i)-65
#         else:
#             answer+=ord('Z')-ord(i)+1
        
#     # 왼쪽,오른쪽 결정
#     if loc[0]>len(name)-loc[-1]:
#         answer+=len(name)-loc[-1]+(loc[-1]-loc[0])
#     else:
#         answer+=loc[0]+(loc[-1]-loc[0])
        
        
    
    
#     return answer

def solution(name):
    answer = 0
    loc=[]
    # A가 아닌 인덱스 위치를 loc 배열에 추가한다
    # for k in name:
    #     if k!='A':
    #         loc.append(name.index(k))

    # enumerate를 이용하여 문자의 위치를 반환(이 때 A는 제외)
    # 참고: index('A')를 사용하면 중복된 문자에 대하여 값반환이 불가
    for i,n in enumerate(name):
        if n!='A':
            loc.append(i)
    
    # 조이스틱의 위,아래에 대한 값을 처리
    for i in name:
        # 위,아래 결정
        if ord(i)-65<ord('Z')-ord(i)+1:
            answer+=ord(i)-65
        else:
            answer+=ord('Z')-ord(i)+1
        
    # 조이스틱의 왼쪽,오른쪽 결정

    length=len(loc)
    # A가 아닌 초기 위치
    answer+=loc[0]
    a=0
    # loc 배열 안에 인덱스 값들이 모두 소진될 때까지 반복해준다
    while True:
        if loc:
            #인덱스 범위값 설정을 위한 length-1까지 조건을 걸어주었다
            if a<length-1:            
                # 오른쪽,왼쪽에 대한 값을 비교하여 오른쪽이면 수열의 차만큼, 왼쪽이면 해당 차만큼을 더해준다
                if loc[a+1]-loc[a]>len(name)-loc[-1]+loc[a]:
                    answer+=len(name)-loc[-1]+(loc[a])
                else:
                    answer+=(loc[a+1]-loc[a])
            else:
                break
        else:
            break
        # 1씩 증가
        a+=1
        
        
    
    return answer



print(solution("JAN"))
