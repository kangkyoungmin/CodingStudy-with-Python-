# 회의실 배정

# 한 개의 회의실이 있다. 여러 회의들이 있는데 스케줄표를 만들고자 한다
# 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있다. 
# 각 회의가 겹치지 않게 하는 회의의 최대 개수?

# 입력부
n=int(input())

time=[]
for i in range(n):
    time.append(list(map(int,input().split())))

# 회의 시작 시간을 기준으로 정렬
# 따라서 종료 시간보다 시작 시간이 늦다면 회의를 사용할 수 있음을 이용
time.sort(key=lambda x:(x[1],x[0])) # key 포인트: 오름차순 정렬 두 번 해야함
stack=time[0][1] #첫번째 배열의 종료 시간을 할당
answer=1
i=1

# stack[i][1] stack[i+1][0]
# 정렬 이후의 반복문 한 번으로 풀 수 있다
# 정렬 하지 않으면 O(N^2)으로 풀어야 한다
while i<n:
    if stack<=time[i][0]: # 종료 시간보다 출발 시간이 더 크면
        answer+=1
        stack=time[i][1]
        # i+=1
    # else: # 종료 시간이 더 큰 경우 다음으로 넘긴다
        # i+=1
    i+=1
    
    # if i==n:
    #     answer_arr.append(answer)
    #     answer=1
    #     stack=time[j][1]
    #     j+=1
    #     i=j

    # if len(answer_arr)==n-1:
    #     break
    
print(answer)

