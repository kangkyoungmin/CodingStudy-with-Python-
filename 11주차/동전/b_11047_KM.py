# 동전 0
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이 때 필요한 동전 개수의 최솟값을 구하는 프로그램
# 만약 주어진 값보다 크면 다음으로 넘어간다

n,price=map(int,input().split())
cnt=0
arr=[]
for i in range(n):
    arr.append(int(input()))

for j in range(n):
    a=arr.pop() # 하나씩 빼낸다
    if a<=price:  # price가 더 크면 수행
        cnt+=price//a # 몫만큼을 count해준다
        price%=a # 몫을 뺀 나머지를 price에 할당해준다
        if price==0: # price가 0이면
            break # break

print(cnt)

