# 서로 다른 옷의 조합의 수를 구하여라
# 두 번째 원소를 key값으로 하여 value값을 찾고, 
# value값의 갯수를 
# def solution(clothes):
#     num=1
#     answer=1
#     temp=False
#     prev=clothes[0][1]
    # clothes.sort(key=lambda x:x[1])
    # for c in clothes: 
    #     if c[1]!=prev:
    #         temp=True
    #         break
    #     prev=c[1]
    # if temp==False:
    #     return len(clothes)

    # for d1,d2 in zip(clothes,clothes[1:]):
    #     print(d1,d2)
    #     if d1[1]==d2[1] and d1[0]!=d2[0]:
    #         num+=1
    #     else:
    #         answer*=num
    #         num=1
    # answer*=num

#     return answer+len(clothes)

# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))


# def solution(clothes):
#     dic={}
#     answer=1
#     visited=[]
#     for c in clothes:
#         dic[c[0]]=c[1]
    
    
#     for d1 in dic:
#         num=1
#         if dic[d1] in visited:
#             continue
#         else: visited.append(dic[d1])
#         for d2 in dic:
#             if dic[d1]==dic[d2]:
#                 num+=1

#         answer*=num
#     return answer-1
        

# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))



def solution(clothes):
    from collections import Counter # 어떤 문자열을 사전형의 리스트로 글자 수 와 함께 반환해준다.
    # Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
    # reduce from functools import reduce 순서형 자료의 원소들을 누적적으로 함수에 적용시킨다. 
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes]) # clothes의 원소가 두 개 있으므로 그 중 두 번째를 선택하겠다는 의미
    print(cnt.values)
    answer = reduce(lambda x, y: x*(y+1), cnt.values(),3) - 1
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
