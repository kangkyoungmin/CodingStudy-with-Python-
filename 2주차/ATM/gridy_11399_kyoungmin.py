# ATM
# 딕셔너리 사용?
# for i in range(3):
#     a[i]=int(input())
# print(a)

n=int(input())

time=list(map(int,input().split())) # 리스트 형태로 받는다
time.sort() # 오름차순으로 정렬
stack=[] # 결과값을 받을 배열 선언
temp=0 # 임시로 데이터를 받는 변수

for data in time: # time 리스트에 있는 데이터 반복문 실행
    temp+=data
    stack.append(temp)

print(sum(stack))
