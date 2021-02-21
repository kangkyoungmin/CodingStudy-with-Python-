# programmers L2 : 소수 찾기
# solved by JY
# DATE : 2021.02.21
# 완전탐색, 순열
# 소수 구하는 방법 (시간복잡도는 O(√N))
# 약수들의 곱으로 봤을때 루트를 씌운 값이 중간값임
# 2에서부터 √N의 값까지 검색하면 이후의 값은 확인할 필요가 없음

import itertools

def find(num):  # num이 소수이면 True 반환
    i = 2
    while i*i <= num:
        if num % i == 0:    # 나머지가 0이면 소수가 아님
            return False
        i += 1
    return True

def solution(numbers):
    answer = 0
    number = []
    for i in range(1, len(numbers)+1):  # 순열을 통해 만들 수 있는 수 조합을 구함
        number += map(int, map(''.join, itertools.permutations(numbers, i)))
    number = set(number)    # 중복 제거를 위한 set 처리

    for n in number:    # 소수 확인을 위한 완전탐색 수행
        if n != 0 and n != 1 and find(n) == True:
            answer += 1

    return answer

# run test
print(solution("17"))  # 3
