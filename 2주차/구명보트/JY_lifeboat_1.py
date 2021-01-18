# programmers L2 : 구명보트
# solved by JY
# DATE : 2020.01.12
# Greedy 알고리즘
# 몸무게가 제일 많이 나가는 친구는 가장 적게 나가는 친구와 나가면 됨
# 단, 합이 limit가 넘지 않음.
# 정확성 통과, 효율성 통과

def solution(people, limit):
    answer = 0
    check = 0
    start = 0
    end = -1
    people.sort(reverse=True)

    while check < len(people):
        if people[start] + people[end] <= limit:    # 같이 갈 사람 구함
            check += 1
            end -= 1
        
        check += 1
        start += 1
        answer += 1

    return answer


# run test
# people = [70,50,80,50]
people = [70, 80, 50]
limit = 100
print(solution(people, limit))