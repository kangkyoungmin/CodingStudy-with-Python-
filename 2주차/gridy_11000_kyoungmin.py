# 강의실 배정
# import heapq
# import sys
# n=int(input())

# room=[]
# for _ in range(n):
#     room.append(list(map(int,sys.stdin.readline().split())))

# 정렬 수행
# room=sorted(room,key=lambda x:[x[1],x[0]])

# 힙 자료구조를 사용한다
# 가장 일찍 끝나는 시간(최소 힙으로 구현)
# 제일 일찍 시작하는 시간
# 둘을 비교하여 시작 시간 < 끝나는 시간인 경우 answer+=1 

# temp=0
# answer=1
# start=[]
# # heapq.heapify(start)

# # heapq.heappush(start,room[0][1])


# 시간 초과 나오는 코드
# 이유는? 리스트에서 min을 쓰면 min의 시간 복잡도가 n이다. 따라서 시간 초과가 나옴

# compare=[]

# for i in range(0,n):
#     if temp<=room[i][0]: #  기존 반만 유지
#         temp=room[i][1]
#     else:
#         answer+=1       # 새로운 반이 개설
#         compare.append(room[i][1])
#         # if temp>room[i][1]:
#         #     temp=room[i][1]
#     if  len(compare)!=0 and temp>min(compare):
#         temp=min(compare)
#         compare.remove(min(compare))

# print(answer)
import heapq
import sys
n=int(input())
compare=[]
room=[]
for _ in range(n):
    room.append(list(map(int,sys.stdin.readline().split())))


room=sorted(room,key=lambda x:x[0]) # 시작하는 시간 기준으로 정렬


# heapq.heappush(compare,room[0][1])

for i in range(n):
    if len(compare)!=0 and room[i][0]>=compare[0]: # 제일 일찍 끝나는 시간과 시작하는 시간을 비교
        heapq.heappop(compare) # 시작이 더 클 경우 수업을 늘릴 필요가 없으므로 pop해준다
    heapq.heappush(compare,room[i][1]) # 힙에 데이터를 추가한다(힙에서 자동으로 min heap으로 정렬)
   


print(len(compare))



        
