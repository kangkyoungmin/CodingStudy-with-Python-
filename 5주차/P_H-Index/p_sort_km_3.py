# H-index

# 논문 n편 중 h번 이상 인용된 논문이 h편 이상, 나머지 논문이 h번 이하 인용되었다면
# h의 최댓값이 이 과학자의 H-index

def solution(citations):
    # citations.sort()
    result=0

    
    if min(citations)>=len(citations): answer=len(citations)

    # h번 이상 인용된 논문이 h편 이상이어야 한다
    for i in range(max(citations),0,-1):
        yes=0
        no=0
        for d in citations:
            if i>=d: # h번 이상 인용되지 않은 
                yes+=1 # 논문의 수
            if d>=i: # h번 이상 인용된 논문
                no+=1  #의 수
            if (yes<=i) & (no>=i):
                result=i
                return max(answer,result)

print(solution([5,5,5,5]))





   # data: h #i: 인용되지 않은 논문의 수
    # 0 1 3 5 6
    # for i,data in enumerate(citations):
    #     if (len(citations)-i)>=data and (data>=i):
    #         result.append(data)
    # answer=max(result)

    # return answer

    #solution 1차원적인 느낌
    # 특정 값보다 클 경우 
    # h번 이상 인용된 논문이 h편 이하일 경우
