# 수 묶기

# 수열의 합을 모두 더해서 구하는 것이 아니라 두 수를 묶어서 더하려고 한다
# 수열이 주어졋을 때 수열의 각 수를 적절히 묶었을 때 그 합이 최대가 되게 하는 프로그램 작성

# solution
# 수 묶기의 규칙을 찾아야 하는 문제
# 양수,양수=곱셈
# 음수, 음수=곱셈

# 0,양수=덧셈
# 0,음수=곱셈

# 1, 양수= 덧셈
# 1, 음수= 덧셈

n=int(input())
arr=[]
answer=0
compare=0
plus=[]
minus=[]
zero=0
one=0

for i in range(n):
    temp=int(input())
    if temp<0:
        minus.append(temp) # 음수인 경우 1로 바꿔준다
    elif temp>1:
        plus.append(temp)
    elif temp==0:
        zero+=1
    else:
        one+=1


plus.sort(reverse=True)
minus.sort()
# for _ in range(zero): # 0의 개수만큼 삭제시켜준다
#     if len(minus)>=3:
#         minus.pop()
#     else:
#         minus.pop(0)

for j in range(0,len(plus),2):
    if j<len(plus)-1: # plus 배열이 마지막 바로 앞의 인덱스값까지만 허용
        answer+=plus[j]*plus[j+1]
    elif j==len(plus)-1:
        answer+=plus[j]

# 마이너스가 짝수개일 경우 0은 의미없다 
# 마이너스가 홀수개일 경우 0을 곱해준다
if len(minus)%2==0:
    for k in range(0,len(minus),2):
        if k<len(minus)-1: # plus 배열이 마지막 바로 앞의 인덱스값까지만 허용
            answer+=minus[k]*minus[k+1]
else:    
    for k in range(0,len(minus),2):
        if k<len(minus)-1: # plus 배열이 마지막 바로 앞의 인덱스값까지만 허용
            answer+=minus[k]*minus[k+1]
        elif k==len(minus)-1 and zero==0:
            answer+=minus[k]

answer+=one

print(answer)








