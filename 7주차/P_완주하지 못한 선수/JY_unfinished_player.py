# programmers L1 : 완주하지 못한 선수
# solved by JY
# DATE : 2021.02.28
# dictionary 사용
# dic = {name : 개수}

def solution(participant, completion):
    dic = {}
    for p in participant:   # participant를 dictionary로 변경
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
        
    for c in completion:    # 완주한 사람들을 개수에서 제거
        if c in dic:
            dic[c] -= 1 

    for d in dic:
        if dic[d] != 0:
            return d

# run test
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # "mislav"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))  # "vinko"
