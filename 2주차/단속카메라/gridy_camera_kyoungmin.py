# 단속카메라
# 모든 차량이 한 번은 단속용 카메라를 만나야한다. 
# roues[i][0]: i번째 차량이 고속도로에 진입한 지점
# routes[i][1]: i번째 차량이 고속도로에서 나간 지점
# 차량의 진입 지점, 진출 지점에 있어도 만난 것으로 간주

# solution
# rouest[i][0]<  point < routes[i][1] 이면 ok
# routes[i][1]번째 배열의 가장 작은 값을 stack을 통해 할당하고 그 값을 다음 인덱스 배열의 [0]값과 비교한다

def solution(routes):

    answer=0

    # 도착지 기준으로 정렬한다
    routes.sort(key=lambda x:x[1])
    # 차량이 1대인 경우는 무조건 1 반환
    if len(routes)==1:
        return 1
    # 카메라 위치에 대한 초기값 설정
    camera=-30001

    for data in routes: # routes에 있는 데이터를 하나씩 꺼낸다
        if camera<data[0]: # 카메라의 위치가 해당 데이터의 출발 지점과 비교하여 작으면 다음으로 이동
            answer+=1 # 1씩 증가시킨다
            camera=data[1] # 카메라의 위치를 해당 데이터의 도착지점으로 둔다
    return answer

    #실패1
    # stack 초기화가 필요하다 
    # while j<len(routes):

        # if j>len(routes)-1: # 한 인덱스의 값이 순회 1회를 실행했을 때 다음 순번으로 이동
        #     break
            # j=i+1 # 기존과 마찬가지로 다음 인덱스값을 대입
            # stack[-1]=routes[i][1] # 스택에 해당값 대입 

        # if stack[-1]>routes[i][1]: # 스택에 있는 값과 다음 순번의 인덱스값을 비교
        #     stack.pop()
        #     stack.append(routes[i][1]) # 스택에 도착지의 최소값을 대입

        # if stack[-1]>=routes[j][0]: # 해당 순번의 도착지와 다음 순번의 출발지를 비교 
        #     answer-=1 # 가능하다면 카메라 설치 대수가 줄어듬
        #     j+=1 # 다음 순번은 가능한지 확인하기 위해 j의 인덱스를 증가시킴
        #     i=j-1
        # else:
        #     # i=j # 해당되지 않는다면 i,j값을 1씩 증가시켜준다
        #     j+=1



        # 실패2

        # camera=data[1]
        # for j in range(i+1,len(routes)):       
        #     if camera>=routes[j][0]:
        #         answer-=1
        #         if data[1]<routes[j][1]:
        #             camera=routes[j][1]
        #     else:
        #         break


print(solution([[-20,15],[-14,-5],[-18,-13],[-5,-3]]))