# 모의고사
#모의고사에 수학 문제를 전부 찍으려함
# 1 2 3 4 5 
# 2 1 2 3 2 4 2 5
# 3 3 1 1 2 2 4 4 5 5  
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순으로 정렬
def solution(answers):
    p_1=[1,2,3,4,5]
    p_2=[2,1,2,3,2,4,2,5]
    p_3=[3,3,1,1,2,2,4,4,5,5]
    

    grade_1=0
    grade_2=0 
    grade_3=0
    #[1,3,2,4,2])
    for i in range(len(answers)):
        if p_1[i%5]==answers[i]:
            grade_1+=1
        if p_2[i%8]==answers[i]:
            grade_2+=1
        if p_3[i%10]==answers[i]:
            grade_3+=1
        
    result=[1] # 결과값을 넣는데 맨 처음에는 첫 번째 학생을 집어넣는다
    compare=[grade_1] 
    if compare[-1]<grade_2: 
        result.pop()
        result.append(2)
        compare.pop()
        compare.append(grade_2)
    elif compare[-1]==grade_2:
        result.append(2)
    if compare[-1]<grade_3: 
        result.pop()
        if not result:
            result.append(3)
        else:
            result.pop()
            result.append(3)
    elif compare[-1]==grade_3:
        result.append(3)
    result.sort()
    
    return result

print(solution([1,3,2,4,2]))

            


