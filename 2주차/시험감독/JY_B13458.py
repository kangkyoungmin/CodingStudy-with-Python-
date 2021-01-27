# baekjoon 13458 : 시험 감독
# solved by JY
# DATE : 2021.01.16

def solution(n, a, b, c):
    answer, check = 0, {}
    for student in a:
        if student in check:
            answer += check[student] 
            continue
        num = 1 # 총감독관
        if student > b :
            num += (student - b) // c
            num += 1 if (student - b) % c > 0 else 0
        answer += num
        check[student] = num

    return answer

# run test
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
print (solution(n,a,b,c))