# 도둑이 마을을 털려고 계획하고 있다
# 도둑이 훔칠 수 있는 돈의 최댓값을 return하도록 한다

# 인접한 두 집을 털면 경보가 울린다
# 각 집에 있는 돈이 담긴 배열 money가 주어질 때 도둑이 훔칠 수 있는 돈의 촤댓값

def solution(money):
    result=[]
    # 돈을 가져갈 수 없는 곳은 그 이전, 그 이후의 값이다
    # 한 번 이상은 무조건 건너 뛰어야 한다
    # 크기 비교가 있어야 한다 한 번 건너뛰고 나서, 

    # 첫 번째 경우: 첫 번째 집부터 시작하여 쭉 돌 경우
    # 두 번째 경우: 마지막 집부터 시작하여 쭉 돌 경우
    # 점화식 찾아내기
    # i가 1씩 더해갈 때마다 i에 해당하는 배열 이전의 값과 i인덱스의 배열값 + i-2 인덱스값을 비교하여
    # 더 큰 것을 배열에 넣어준다

    def solution(money):
        dp1 = [0] * len(money)
        dp1[0] = money[0] # 첫 집부터 털기 위해 세팅
        dp1[1] = max(money[0], money[1]) # 첫 번째 값과 다음 값을 비교

        for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
            dp1[i] = max(dp1[i-1], money[i]+dp1[i-2]) # 이전값과 다음 값을 더했을 때를 비교한다

        dp2 = [0] * len(money)
        dp2[0] = 0
        dp2[1] = money[1]

        for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
            dp2[i] = max(dp2[i-1], money[i]+dp2[i-2]) # 

        return max(max(dp1), max(dp2)) # 두 경우 중 최대

print(solution([1,2,3,1]))
