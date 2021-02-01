# 징검다리
# 출발지점부터 distance만큼 떨어진 곳에 도착지점이 있다
# rocks: 바위의 위치를 담은 배열
# n: 몇 개를 뺼 것인가
# distance 목표 지점

# solution
# start,end,mid로 나누어 지점을 찾는다
# 무엇을 우선으로 빼야하는가? 
# 각 지점 사이의 거리의 최솟값 중에 가장 큰 값?
# 2개를 랜덤으로 뽑아서 제거한다. 그 후 각 바위 사이의 거리를 배열에 추가한다
# 이 때 최솟값을 배열에 넣고 해당 배열의 min값이 정답이 된다

# solution#2
# distance를 배열 안에 넣는다
# 


# def solution(distance, rocks, n):
#     if len(rocks)<=n:
#         return -1

#     def count(num):
#         count=0
#         while num>0:
#             if (num&1)==1: count+=1
#             num=num>>1
#         return count
    
#     def calc(rock):
#         temp=rock[1]-rock[0]
#         for i in range(len(rock)-1):
#             result=rock[i+1]-rock[i]
#             if result<temp:
#                 result=temp
#         return result

            

#     def comb(rocks,n,distance): # 배열 중에 n개만큼을 제외하는 경우
#         result=[]
#         real_result=[]
#         for i in range(0,1<<len(rocks)):
#             if count(i)==(len(rocks)-n):
#                 for j in range(0,len(rocks)):
#                     if i&(1<<j)!=0:
#                         result.append(rocks[j])
#                 result.sort()
#                 result.append(distance)
#                 real_result.append(calc(result))
#                 result.clear()
#         return min(real_result)





#     return comb(rocks,n,distance)

# print(solution(25,[2,14,11,21,17],2))

# def solution(distance, rocks, n):
#     if len(rocks)<=n:
#         return -1
#     result=[]
#     V= [0] * len(rocks)
#     real_result=[]

#     def calc(rock):
#         temp=rock[1]-rock[0]
#         for i in range(len(rock)-1):
#             result=rock[i+1]-rock[i]
#             if result<temp:
#                 result=temp
#         return result

#     def f(idx,cnt):
#         if cnt>len(rocks)-n: #rocks-n개보다 더 커지면 탈출 
#             return
#         if cnt==len(rocks)-n: # 징검다리에서 돌을 n개만큼 제거한 것고 같을 떄
#             for i in range(0,len(rocks)): 
#                 if V[i]: result.append(rocks[i]) # 인덱스가 True이면 append시킨다
#             result.append(distance)
#             real_result.append(calc(result))
#             result.clear()
#         if cnt>len(rocks)-n or idx==len(rocks):
#             return

#         V[idx]=True
#         f(idx+1,cnt+1)

#         V[idx]=False
#         f(idx+1,cnt)

#     f(0,0)
#     return min(real_result)

# print(solution(25,[2,14,11,21,17],2))
import math
def solution(distance,rocks, n):
    answer=0
    start,end=0,distance
    rocks=sorted(rocks)
    rocks.append(distance)
    rnum=len(rocks)
 
    while start<=end: # 이분탐색을 위한 탐색조건
        remove=0
        prev=0
        min_inter=math.inf
        mid = (start+end)//2 # 
 
        for i in range(rnum):
            if rocks[i]-prev < mid:  #rocks[i]-prev가 inter값
                remove+=1 #바위제거
                
            else : #바위 제거 안할경우 
                min_inter=min(min_inter,rocks[i]-prev) #inter값 갱신.
                prev=rocks[i] #현재 바위위치를 prev로
 
        #너무 많이 제거되었을 경우, 기준을 높여서 제거를 줄여야함
        if remove > n:
            end=mid-1
        #적게 제거되었을 경우, 기준을 낮춰서 제거를 늘려야함
        else:
            answer=min_inter
            start=mid+1
            
    return answer

    
