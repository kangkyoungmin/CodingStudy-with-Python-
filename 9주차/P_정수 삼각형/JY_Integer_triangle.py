# programmers L3 : 정수 삼각형
# solved by JY
# DATE : 2021.03.11
# DP 사용. Triangle 배열 사용
# 위에서부터 내려오면서 더한 값을 저장하여 정답 도출

def solution(triangle):    
    for line_idx in range(1, len(triangle)):
        triangle[line_idx][0] += triangle[line_idx-1][0]
        triangle[line_idx][-1] += triangle[line_idx-1][-1]
        
        for num_idx in range(1, len(triangle[line_idx]) - 1):  # 위에 2개 확인 > 큰 수랑 합치기
            triangle[line_idx][num_idx] += max(triangle[line_idx-1][num_idx-1], triangle[line_idx-1][num_idx])

    return max(triangle[-1])

# run test
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]), 30)