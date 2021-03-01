# programmers L2 : 위장
# solved by JY
# DATE : 2021.02.28
# dictionary 이용
# dic = { 종류 : [이름] }

def solution(clothes):
    answer = 0
    dic = {}
    for name, kind in clothes:  # dic 생성
        if kind in dic:
            dic[kind].append(name)
        else:
            dic[kind] = [name]

    for d in dic:
        if answer != 0:
            answer += answer * len(dic[d])  # 이전 종류들 갯수(answer)에 현재 종류(len(dic[d])를 추가
        answer += len(dic[d])   # 현재 종류 중 1개만 입는 경우 추가

    return answer

# run test
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))   # 5
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))   # 3
print(solution([["a", "face"], ["b", "face"], ["c", "face"], ["aa", "f"], ["bb", "f"], ["A", "F"], ["B", "F"]]))   # 35