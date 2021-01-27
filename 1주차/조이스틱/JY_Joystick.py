# programmers L2 : 조이스틱
# solved by JY
# DATE : 2021.01.11
# Greedy 알고리즘

def change(c):
    if ord(c) - ord('A') < 13:
        return ord(c) - ord('A')
    else:
        return ord('Z') - ord(c) + 1

def solution(name):
    name = list(name)
    answer = 0
    right = 0
    left = 0
    cur = 0

    while True :
        # 더이상 바꿀 것이 없음 > break
        if name.count('A') == len(name):
            break

        # cur 기준 오른쪽 방향 가장 가까운 곳
        while cur + right < len(name):
            if name[cur + right] != 'A':
                break
            right += 1

        # cur 기준 왼쪽 방향 가장 가까운 곳
        while cur + left < len(name):
            if name[cur - left] != 'A':
                break
            left += 1

        # 오른쪽 방향으로 이동
        if right <= left:
            answer += right + change(name[cur + right])
            name[cur + right] = 'A'
            cur = cur + right
        # 왼쪽 방향으로 이동
        else :
            answer += left + change(name[cur - left])
            name[cur - left] = 'A'
            cur = cur - left
        right = 0
        left = 0

    return answer

# run test
print(solution("ABABAAAABA"))

