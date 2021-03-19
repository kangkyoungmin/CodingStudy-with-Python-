# programmers L2 : 메뉴 리뉴얼
# solved by JY
# DATE : 2021.03.17
# 조합 이용
# 각 orders에서 원하는 course만큼 조합 구하기> dictionary에 저장
# max_c : 각 course에서 max값 저장용 (2개 코스 중에서 최댓값은 4이면 max_c[2]=4)

import itertools
import collections

def solution(orders, course):
    answer = []
    orders = [''.join(sorted(st)) for st in orders]
    dic = collections.defaultdict(int)
    for c in course:
        for menu in orders:
            for com in list(itertools.combinations(menu, c)):
                com = ''.join(com)
                dic[com] += 1
    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    max_c = collections.defaultdict(int)
    for st, num in dic:
        if max_c[len(st)-1] == 0:
            answer.append(st)
            max_c[len(st)-1] = num
        elif max_c[len(st)-1] == num:
            answer.append(st)
        elif num == 1:
            break

    answer.sort()
    return answer

# run test
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]), ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]), ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]), ["WX", "XY"])