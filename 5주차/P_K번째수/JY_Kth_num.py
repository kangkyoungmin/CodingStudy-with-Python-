# programmers L1 : K번째수
# solved by JY
# DATE : 2021.02.05
# 정렬. sort() 이용
# 조건에 맞게 따로 복사 후 정렬, k번째 수 확인

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        tmp = array[commands[i][0]-1:commands[i][1]]
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])

    return answer

# run test
import sys
input = sys.stdin.readlines
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])) # [5, 6, 3]
