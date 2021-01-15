# programmers L2 : 구명보트
# DATE : 2020.01.15
# Greedy 알고리즘



# 1. 무거운 순서대로 정렬
# 2. 가장 무거운 사람 + 가장 가벼운 사람 < limit?

def soultion(people, limit):
    people.sort(reverse=True) #무거운 사람부터 정렬(내림차순)
    heavy_index = 0
    light_index = len(people) - 1
    count = len(people) #한 명씩 보트 타는 걸 기준으로 함 / 두명씩 타는 경우 -1
    while heavy_index < light_index: #heavy = end : 무게 비교할 필요 x
        if people[heavy_index] + people[light_index] <= limit: # 두 명 같이 타는 경우
            light_index -= 1 # 인덱스 한칸 앞으로
            count -= 1
        heavy_index += 1 # 다음 무거운 사람으로
    return count
