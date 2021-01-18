# 구명보트
# 한 번에 최대 2명씩 탈 수 있다. 무게 제한도 있다.
# 구명보트의 개수를 최소화해야한다
# 구명보트 개수의 최솟값은?

# n=1~5000 시간복잡도 nlogn~n^2정도
# 몸무게는 40~240
# 구명보트의 무게 제한: 40~240kg
# 구몁오트의 무게 제한 > 사람들의 몸무게 중 최댓값

# #1먼저 주어진 배열을 정렬한다 그리고 초기 answer로 최대 보트 수만큼을 넣어준다
# #2정렬된 리스트 내에서 가장 큰 값과 가장 작은 값을 더하여 해당 값이 limit보다 작을 경우 answer-1을 해준다 

def solution(people,limit):
    answer=len(people) # 최대 보트의 갯수
    
    #1먼저 주어진 배열을 정렬한다 그리고 초기 answer로 최대 보트 수만큼을 넣어준다
    people.sort(reverse=True) # 전체를 sort 시킨다
    # m: max값, n: min값
    m,n=0,len(people)-1
 
    #2정렬된 리스트 내에서 가장 큰 값과 가장 작은 값을 더하여 해당 값이 limit보다 작을 경우 answer-1을 해준다 
    while m<n:
        if people[m]+people[n]<=limit:
            answer-=1
            n-=1
        else:
            m+=1
            continue
        m+=1
        
    return answer
        


print(solution([70,80,50],100))

