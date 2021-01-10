def solution(n, lost, reserve):
    # 잃어버리고 여벌이 있는 학생들 (교집합)
    lostAndReserve = set(lost) & set(reserve)
    # lost에만 있는 학생들
    lost2 = set(lost) - set(reserve)
    # reserve에만 있는 학생들
    reserve2 = set(reserve) - lostAndReserve

    # reserve2에서 체육복 줄 수 있는 학생들 찾기
    # x-1이 lost2에 있으면 삭제
    # 없다면 x+1이 있는지 확인, 있으면 삭제
    for x in reserve2 :
        if x-1 in lost2:
            lost2.remove(x-1)
        elif x+1 in lost2:
            lost2.remove(x+1)

    answer = n - len(lost2)
    return answer
