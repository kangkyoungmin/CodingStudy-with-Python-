def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
