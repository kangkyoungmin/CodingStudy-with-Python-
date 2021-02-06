# programmers L2 : 가장 큰 수
# solved by JY
# DATE : 2021.02.05
# 정렬. sort() 이용
# 1 > 1111
# 12 > 1212
# 123 > 1233
# 1000 > 1

def solution(numbers):
    tmp = [str(n) for n in numbers]
    
    tmp.sort(key=lambda x: x[0]*4 if len(x) == 1 else (x*2 if len(x) == 2 else (x+x[2] if len(x) == 3 else "1")), reverse=True)
    # t = list(map(lambda x: x[0]*4 if len(x) == 1 else (x*2 if len(x) == 2 else (x+x[2] if len(x) == 3 else "1")), tmp)) // 확인 코드
    # print(tmp, '\n',t)

    return ''.join(tmp[idx] for idx in range(len(tmp))) if sum(map(int, tmp)) > 0 else '0'

# run test
import sys
input = sys.stdin.readlines
print(solution([6, 10, 2]) == "6210") 
print(solution([3, 30, 34, 5, 9]) == "9534330") 
print(solution([3, 36, 361, 34, 5, 9, 344, 336, 335, 347, 56, 369]) == "956536936361347344343363353")
print(solution([0, 0, 0, 0, 0]) == "0")
print(solution([21,212]) == "21221")
print(solution([12,121]) == "12121")
print(solution([0, 5, 10, 15, 20]) == "52015100")
print(solution([1000, 0, 5, 99, 100, 1]) == "995110010000")
print(solution([40, 403]) == "40403")
print(solution([40, 404]) == "40440")
print(solution([40, 405]) == "40540")
print(solution([3, 30, 34, 5, 9, 4, 40, 42]) == "954424034330")