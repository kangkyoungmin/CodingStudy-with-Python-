# 로프는 그 굵기나 길이가 다르기 떄문에 들 수 있는 물체의 중량이 서로 다르다
# 여러 개의 로프를 병렬로 연결하면 각 로프ㅔ 걸리는 중량을 나눌 수 있다
# k개의 로프를 사용하여 중량이 w인 물체를 들어올린다. 각 로프에는
# 모두 고르게 w/k만큼의 중량이 걸리게 된다
# 임의로 몇 개의 로프를 골라서 사용해도 된다
n=int(input()) # 로프의 개수를 입력받는다
queue=[]
result=[]
# 비교하는데 가장 작은 값부터 n,n-1,n-2이런식으로 곱해질 수 있다
for i in range(n):
    queue.append(int(input()))
queue.sort(reverse=True)
for i in range(0,n):
    result.append(queue[i]*(i+1))

print(max(result))

