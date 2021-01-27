# baekjoon 12845 : 모두의 마블
# solved by JY
# DATE : 2021.01.17
# Greedy 알고리즘

def solution():
    level = [card[0] + card[i] for i in range(1, n)]
    return sum(level)

# run test
n, card = int(input()), list(map(int, input().split()))
card.sort(reverse=True)
print(solution())