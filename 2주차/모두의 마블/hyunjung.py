# Baekjoon Online Judge : 모두의 마블
# DATE : 2020.01.16
# Greedy 알고리즘



# 가장 높은 레벨은 남아있고 주변 카드가 와서 합쳐짐
# 레벨이 가장 높은 카드는 끝까지 남아있음
# 나머지 카드는 전부 레벨이 가장 높은 카드와 합쳐짐

n = int(input())
level = list(map(int, input().split()))

level.sort(reverse=True) # 내림차순 정렬
gold = 0
for i in range(1,n):
    gold += level[0] + level[i]
print(gold)

# 3 / 30 40 40 / 140
