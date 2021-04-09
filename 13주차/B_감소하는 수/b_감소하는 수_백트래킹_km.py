# [사용한 알고리즘]

# 백트랙킹(backtracking)

 

# [알고리즘]

# 1. 0부터 수를 증가시키면서 N번째 감소하는 수를 찾을 때까지 2, 3번 과정을 반복합니다.

# 2. 현재 수가 감소하는 수이면 현재 수 + 1을 수행합니다.

# 3. 현재 수가 감소하는 수가 아니면 감소하지 않는 위치가 감소하도록 수정합니다.

# 4. N번째 감소하는 수를 찾으면 출력합니다.

 

# ※ N이 1022일 때 9876543210이므로 1023부터는 -1을 출력합니다.

import sys

sys.setrecursionlimit(10 ** 9)


def solve(n):
    cnt = 0
    num = 1
    while True:
        str_num = str(num) # 문자열로 정의해준다
        print(str_num)
        flag = True
        if len(str_num) == 1:  # 길이가 1이면 무조건 감소하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i - 1]): # 앞이 더 크면 넘겨준다
                    continue
                else: # 감소하지 않는 경우 
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:  # n번째 감소하는 수
                return num
            num += 1


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    if n >= 1023:  # 1022: 9876543210
        print(-1)  # N번째 감소하는 수 x
    elif n == 0:
        print(0)
    else:
        print(solve(n))