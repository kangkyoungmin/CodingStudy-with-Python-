# 시험 감독
import math
# 입력 받기
n=int(input()) # n: 시험장 수

a=list(map(int,input().split())) # a:응시자 수

b,c=map(int,input().split()) # b: 총감독관 c: 부감독관

# 총감독관은 시험장마다 1명 
# a 각 배열마다 필요한 감독관은 a-b(1)-c*(result-1)=0

# 
result=0

for data in a:
    if (data-b)>=0: # 학생 수가 총감독관 케어 수보다 많을 경우
        result+=math.ceil((data-b)/c) # 부감독관 수를 더해준다
        result+=1 # 총감독관 1을 더해준다
    else:
        result+=1 # 총감독관만 더해준다

print(result)


