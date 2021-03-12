# 정수삼각형 시간복잡도 줄이기

def solution(triangle):
    # solution
    # triangle에 있는 값들이 배열로 다 저장되어 있다
    # 이를 어떻게 이용할 지가 중요하다
    # 이 문제의 포인트? 삼각형의 높이의 최댓값은 500이다

    # i가 len(triangle)에 도달하지 않을 때까지 while문을 통해 반복해서 triangle[i]에 있는 데이터들을 더해준다
    temp=[[] for x in range(len(triangle))]
    temp[0]=triangle[0]
    
    # 대각선 쪽으로 한 칸 오른쪽 또는 왼쪽으로만 이동이 가능하다
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j==0:
                triangle[i][j]=triangle[i-1][j]+triangle[i][j]
            elif j==i:
                triangle[i][j]=triangle[i-1][j-1]+triangle[i][j]
            else:
                triangle[i][j]=max((triangle[i-1][j-1],triangle[i-1][j]))+triangle[i][j]

    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

def solution(triangle):
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer

def f(triangle, i, j, memo):
    if i == len(triangle)-1:
        return triangle[i][j]

    if (i,j) in memo:
        return memo[(i,j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i,j)] = x

    return x

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
