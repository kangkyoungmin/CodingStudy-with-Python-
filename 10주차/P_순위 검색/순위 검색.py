# 언어 직군 경력 소울 푸드 점수
# split 명령어를 통해 and를 기준으로 자른다
# info 또한 split으로 공백을 기준으로 자르고 이를 2차원 배열로 표현한다
# 2차원 배열은 초기에 값을 할당해주고 기준은 열을 기준으로 한다
# - 이면 어떠한 것도 상관없다

def solution(info, query):

    i_arr=[]
    q_arr=[]
    result=[]
    
    for i in range(len(info)):
        i_arr.append(info[i].split(' '))
        temp=query[i].split(' and ')
        temp2=temp[-1].split(' ')
        temp3=temp[:-1]+temp2
        q_arr.append(temp3)
    # key,value형식으로 변환해주는 작업을 거친다
    # key값으로 언어,직군,경력,소울 푸드를 넣고 value로 점수를 넣어준다
    # -가 존재할 때와 존재하지 않을 떄를 고려하여 key값으로 정의한다.
    # search 시에는 효율성을 위해 bisect를 사용해준다
    
    for q in q_arr: # 쿼리를 하나씩 비교
        count=0
        for i in range(0,len(info)):
            check=0
            for j in range(5):
                if 0<=j<=3 and q[j]=='-': # 예외 케이스 스킵
                    continue

                if 0<=j<=3:
                    if i_arr[i][j]==q[j]:
                        continue
                    else:
                        check=1
                        break   

                elif j==4: 
                    if int(i_arr[i][j])>=int(q[j]):
                        continue
                    else:
                        check=1
                        break
            if check==0:
                count+=1
        result.append(count)
    return result

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))