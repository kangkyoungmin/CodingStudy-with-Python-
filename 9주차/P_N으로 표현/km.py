dic = {0: 1} # 사전형을 하나 정의

def DP(result, level, array, target):
    if level < 9: # 9보다 작은 수 (최솟값이 9보다 작다)
        if result in dic:
            if dic[result] > level:
                dic[result] = level
                if result == target:
                    return level
                for i in range(0, 8):
                    DP(result-array[i], level + i+1, array, target)
                    DP(result//array[i], level + i+1, array, target)
                    DP(result*array[i], level + i+1, array, target)
                    DP(result+array[i], level + i+1, array, target)
        else:
            dic[result] = level
            if result == target:
                return level
            for i in range(0, 8):
                DP(result-array[i], level + i+1, array, target)
                DP(result//array[i], level + i+1, array, target)
                DP(result*array[i], level + i+1, array, target)
                DP(result+array[i], level + i+1, array, target)
            
def solution(N, number):
    answer = 0
    array = []
    your_dict = {0: 1}
    num = N
    for i in range(0, 8):
        array.append(num)
        num = num*10 + N
    DP(0, 0, array, number)
    if(number in dic):
        answer = dic[number]
    else:
        answer = -1
    return answer

# 보텀업 방식을 이용한 풀이

def solution(N, number):
    # solution
    # 해당 level이 올라갈 때마다 level에 관한 값들을 모두 level을 키로 한 value값으로 넣어준다
    # 이전 레벨들끼리의 합을 통해 level을 만들어 그 값이 target과 일치할 경우 빠져나간다
    s=[set() for x in range(8)]
    for i,x in enumerate(s):
        x.add(int(str(N)*(i+1)))
    


    for i in range(0,8): # level 설정
        for j in range(i):
            for val1 in s[j]:
                for val2 in s[i-j-1]:
                    s[i].add(val1+val2)
                    s[i].add(val1-val2)
                    s[i].add(val1*val2)
                    if val2!=0:
                        s[i].add(val1//val2)
        if number in s[i]:
            return i+1
        
        




print(solution(5,12))

