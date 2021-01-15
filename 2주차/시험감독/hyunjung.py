# Baekjoon Online Judge : 시험감독
# DATE : 2020.01.15
# Greedy 알고리즘

N = int(input()) # 시험장의 개수 입력받기
tester = list(map(int, input().split())) # 각 시험장의 응시자 수 입력받음
B, C = map(int, input().split()) # 총감독관(B), 부감독관(C)의 수 입력받음


# 총감독관 1명 / 부감독관 여러명
count = 0 # 감독관의 수
for i in tester:
    i -= B  # 각 시험장에서 총 감독이 감독 가능한 인원 뻄
    count += 1
    if i >= 0: # 보조감독이 몇 명 들어갈지
        if i % C != 0:
            count += (i//C) + 1
        else:
            count += (i//C)
print(count)
