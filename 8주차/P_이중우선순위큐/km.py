import heapq
def solution(operations):
    answer = [0,0]
    heap=[]
    heapq.heapify(heap)
    delete_heap=0
    operation=["I","D 1","D -1"]

    def heap_change(heap):
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
        list(heap)
    if len(heap)>=2:
        return [max(heap),min(heap)]
    elif len(heap)==1:
        return [heap[0],0]
    else:
        return [0,0]
        
    
    return heap
  
 # 좋은 풀이 코드
from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1": 
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num) # max_heap으로 구현
            heappush(min_heap, num) # min_heap으로 구현
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]
