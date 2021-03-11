# 큐가 비어있으면 [0,0]
# 큐가 비어있지 않으면 [최댓값,최솟값]을 return

# sol
# 명령어에 해당하는 배열을 만든다
# 명령어 D 1이 등장하면 최대힙으로 구성하여 최댓값 삭제
# 명령어 D -1이 등장하면 최소힙으로 구성하여 최솟값 삭제

# 빈 큐에 데이터를 삭제하라는 연산은 무시
# 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우 하나만 삭제
import heapq
def solution(operations):
    answer = [0,0]
    heap=[]
    heapq.heapify(heap)
    delete_heap=0
    operation=["I","D 1","D -1"]

    def heap_change(heap): # 최소 -> 최대, 최대 -> 최소로 변경해주는 함수
        list(heap)
        print(heap)
        for i in range(len(heap)):
            heap[i]=-heap[i]
        heapq.heapify(heap)

    for o in operations:
        if o[0]==operation[0]:
            heapq.heappush(heap,int(o[2:]))
        elif o=="D 1":
            if len(heap)==0:
                continue
            heap_change(heap)
            print(heap[0])
            heapq.heappop(heap)
            if len(heap)>0:
                heap_change(heap)

        elif o=="D -1":
            if len(heap)==0:
                continue
            heapq.heappop(heap)
        list(heap) # max,min 메소드를 사용하기 위해 list로 변경
    if len(heap)>=2:
        return [max(heap),min(heap)]
    elif len(heap)==1:
        return [heap[0],0]
    else:
        return [0,0]
        
    
    return heap

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))

# solution2 좋은 풀이법
# from heapq import heappush, heappop

# def solution(arguments):
#     max_heap = []
#     min_heap = []
#     for arg in arguments:
#         if arg == "D 1": 
#             if max_heap != []:
#                 heappop(max_heap)
#                 if max_heap == [] or -max_heap[0] < min_heap[0]:
#                     min_heap = []
#                     max_heap = []
#         elif arg == "D -1":
#             if min_heap != []:
#                 heappop(min_heap)
#                 if min_heap == [] or -max_heap[0] < min_heap[0]:
#                     max_heap = []
#                     min_heap = []
#         else:
#             num = int(arg[2:])
#             heappush(max_heap, -num) # max_heap으로 구현
#             heappush(min_heap, num) # min_heap으로 구현
#     if min_heap == []:
#         return [0, 0]
#     return [-heappop(max_heap), heappop(min_heap)]
            



