# 완전탐색 카펫
# 가로 길이가 세로 길이보다 길다
# brown과 yellow를 합하게 되면 return값(가로*세로)과 동일해야한다

# solution
# 가로 *2 +세로 *2 -4 한 것이 테두리 부분 = brown
# 나머지 부분 = yellow

# 쌍을 구해야 한다
# 12=4*3 2*6 1*12
def solution(brown, yellow):

    num=brown+yellow
    com_br=0
    com_ye=0
    if brown>=yellow: # iteration의 범위 정하기
        iter=brown
    else:
        iter=yellow

    for i in range(1,iter+1):
        j=num//i # i*j=brown+yellow를 이용
        if num%i==0 and i>=j: 
            com_br=2*(i+j)-4
            com_ye=i*j-com_br
        if com_br==brown and com_ye==yellow: # 둘레의 길이 이용
            return [i,j]

    # for n in result:
    #     com_br=n[0]*2+n[1]*2-4
    #     com_ye=(n[0]*n[1])-com_br
    #     if com_br==brown and com_ye==yellow:
    #         return [n[0],n[1]]
