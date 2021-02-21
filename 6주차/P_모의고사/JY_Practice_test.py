# programmers L1 : 모의고사
# solved by JY
# DATE : 2021.02.19
# 완전탐색

def solution(answers):
    answer = [0] * 3
    check = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for idx in range(len(answers)):
        if answers[idx] == check[0][idx % 5]:   # 1번 수포자 정답 확인
            answer[0] += 1
        if answers[idx] == check[1][idx % 8]:   # 2번 수포자 정답 확인
            answer[1] += 1
        if answers[idx] == check[2][idx % 10]:  # 3번 수포자 정답 확인
            answer[2] += 1

    answer_max = max(answer)    # 가장 많이 맞춘 정답 수
    answer = [idx + 1 for idx in range(3) if answer[idx] == answer_max] # 가장 많이 맞춘 사람 확인

    return answer

# run test
print(solution([1,2,3,4,5]))    # [1]
print(solution([1,3,2,4,2]))    # [1,2,3]


