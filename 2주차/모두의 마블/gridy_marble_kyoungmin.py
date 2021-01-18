# 모두의 마블 문제

# 골드를 최대한 많이 받을 수 있도록 한다
# 붙이는 조건
# 인접한 카드이며, 업그레이드된 카드 A의 레벨은 변하지 않음
# 카드 합성 시 두 카드 레벨의 합만큼 골드를 받는다

# 입력
import sys
# from collections import deque
n=int(input())
card=list((map(int,sys.stdin.readline().split())))

# 솔루션
# 규칙을 찾아서 문제를 해결한다
# max값을 찾고, 카드 총합과 (카드 장수-2)*max 한 것을 곱한 것을 더해준다

max_data=max(card)    
for i,data in enumerate(card):
    if(data==max_data):
        index=i

result=card[index]*(len(card)-2)+sum(card)
            
print(result)



# 솔루션
# deque 사용해서 오른쪽에서는 push, 왼쪽에서는 popleft
# 왼쪽,오른쪽에 있는 값을 비교하여 더 큰 값과 더한다
# 스택 구조를 떠올렸을 때 len(stack)==3 비교 수행 

# dq=deque()
# answer=0
# for c in card:
#     dq.append(c)

#     if len(dq)==3:
#         if dq[0]<dq[2]:
#             answer+=dq[1]+dq[2]
#             dq[1]=dq[2]
#             dq.pop()
#         else:
#             answer+=dq[0]+dq[1]
#             dq[1]=dq[0]
#             dq.popleft()

# if len(dq)!=1:
#     for d in dq:
#         answer+=d

# print(answer)

# max값의 인덱스를 찾고 해당 인덱스의 양 옆의 값을 더하고 나머지는 max값과 동일하게 처리하므로
# (배열의 길이-2) * max값 + 양 옆 = result
