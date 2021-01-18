# 멀티탭 스케줄링
from sys import stdin

# n: 멀티탭 구멍의 개수 k: 전기 용품의 총 사용횟수
# input 부분
n,k=map(int,input().split())
# 전기용품의 이름이 k 이하의 자연수로  사용순서대로 주어진다
array=list(map(int,stdin.readline().split()))

# 미래의 경우에서 해당사항이 없는 것을 우선순위로 뺸다
# 만약에 미래의 경우에 모든 것들이 해당사항이 있을 경우는 나머지들을 모두 경우에 포함시킨다

# 스택을 이용해준다
stack=[0] * n

answer=0
# check=[] # 이후 배열에 스택에 넣어진 값이 있는지 확인하는 배열

for i,data in enumerate(array):

    if len(array)<n:
        break

    # 만약 스택이 비어있을 경우
    if 0 in stack:
        stack[i]=data
        continue   
    # 만약 스택 안에 데이터가 있을 경우
    if data in stack:
        continue
    else:
        if len(stack)==n: # 스택이 다 차 있을 경우 stack[::-1] 역순 배열 iterator
            # if data not in array[i:]:
            #     stack.remove(data)
            check=[]

            for stack_data in stack: 
                if stack_data not in array[i:]: # 사용되지 않는 플러그가 존재하는 경우 우선적으로 제거
                    #  stack.remove(stack_data)
                    # break
                    check.append(stack_data)
            #  사용되지 않는 플러그가 존재하는 경우
            if len(check)>0:
                for array_data in reversed(array[i:]): # 사용되지 않는 플러그가 존재하는 경우 우선적으로 제거
                    if array_data in check:
                        stack.remove(array_data)
                        break
            # 사용되지 않는 플러그가 존재하지 않는 경경우
            else:
            #  꽂혀있는 플러그 중 가장 나중에 사용되는 플러그를 뽑아준다
                for array_data in reversed(array[i:]):
                    if array_data in stack:
                        stack.remove(array_data)
                        break                       
        stack.append(data)
        answer+=1
print(answer)

