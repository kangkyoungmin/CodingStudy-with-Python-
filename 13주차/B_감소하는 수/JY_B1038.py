# baekjoon 1038 : 감소하는 수
# solved by JY + hint
# DATE : 2021.04.09
# Queue 사용
# front의 마지막 자리숫자보다 작은 수들을 붙여가며 que 생성

from sys import stdin
input = stdin.readline
N = int(input())
que = ['0','1','2','3','4','5','6','7','8','9']
cnt = 0
while que:
    front = que.pop(0)
    if cnt == N:
        print(front)
        exit()
    cnt += 1
    for i in range(int(front[-1])):
        que.append(front + str(i))
print(-1)