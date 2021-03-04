# 주식 가격
# prices 배열에서 해당 배열을 순회하면서
# 해당 인덱스 이후의 값들이 크거나 같으면 가격이 떨어지지 않은 것으로 간주되어 num+1이 된다
# 
def solution(prices):
    answer = []

    for i in range(len(prices)):
        j=i+1
        num=0
        while j<len(prices):
            num+=1
            if prices[i]>prices[j]:
                break
            j+=1
        answer.append(num)
    return answer


print(solution([1,2,3,2,3]))
