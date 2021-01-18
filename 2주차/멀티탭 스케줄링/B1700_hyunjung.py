# Baekjoon Online Judge : 멀티탭 스케줄링
# DATE : 2020.01.18
# Greedy 알고리즘


# -멀티탭에 빈 플러그 있다면 -> 꽂으면 됨 -> continue해 다음기기 확인
# -사용하려는 제품이 이미 꽂혀 있으면 -> 넘어감 -> continue해 다음기기 확인
# -멀티탭에 새로 꽂아야하는데 빈 플러그가 없는 경우 -> 적당한 플러그 빼야 함
#   현재 꽂혀 있는 전자제품 중 처음으로 사용되는 시점이 늦은 플러그 빼야 함

N, K = map(int, input().split()) # 멀티탭 구멍의 개수, 전기용품의 총 사용횟수
item = list(map(int, input().split())) # 용품 사용 순서대로

plug = []  # 현재 멀티탭
count = 0

for i in range(K):
    if item[i] in plug : # 이미 꽃혀있다면
        continue
    if len(plug) < N: # 멀티탭에 빈 플러그 있다면
        plug.append(item[i])
        continue

    else : # 빈 플러그가 없으면 현재 꽂혀 있는 아이템 중 가장 늦게 사용하는 아이템을 뽑음
        temp = list(plug)
        for j in range(i+1, K): # 이미 꽂혀있는 용품의 다음 사용 순서 찾기
            if len(temp) == 1:
                break
            if item[j] in temp: #
                temp.remove(item[j]) # 다시 사용되는 용품을 temp에서 제거
        plug.remove(temp[0]) # temp에는 다시 사용 안 하는 용품 남았으니 뽑고 새로운 용품 꽂음
        count += 1
        plug.append(item[i])

print(count)
