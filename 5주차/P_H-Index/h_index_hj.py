def solution(citations):
    h_index = 0 #논문이 제출되면 0번인용횟수 가진 논문은 0개 이상
    n = len(citations)
    citations.sort() # 오름차순
    for i, j in enumerate(citations): #i번째 인용횟수가 남은 논문의 수보다 많을떄 h_index결정
        if j >= (n - i):
            h_index = (n - i)
            break
    return h_index
