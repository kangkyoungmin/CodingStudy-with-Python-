# 입국심사
# 모든 사람이 심사를 받는 데 걸리는 시간의 최솟값

def solution(n,times):
    answer=0  
    times.sort()
    cp_times=times[:]


    # solution 
    # times 배열의 원소가 몇 개인지를 확인하고 해당 원소의 개수만큼 n에서 빼준다 
    # 나머지도 1씩 n을 빼는데 times배열의 첫 번째 인덱스부터의 원소의 값을 더해준다

    # 정렬 작업을 수행하고, max(times)
    # times의 배열의 수를 늘리고 이를 통해 값을 찾는다?
    # max값보다 작으면 추가시킨다?

    def solution(n,times):
        right=min(times)*n # 최대값은 times배열에서 가장 작은 심사대에서 모두 심사받는 경우
        left=1 # 가장 최소인 경우

        answer=0
        while(left<=right): # 왼쪽은 작은 경우, 오른쪽은 큰 경우로 생각 
            mid=(right+left)//2 # 반으로 쪼개는 경우로 생각
            temp=n 
            for i in times:
                temp-=mid//i # 나눈 몫을 비교하여 뺀 값이 0이면 답이 나오게 된다
                if temp<=0:
                    answer=mid
                    right=mid-1 # 이분법으로 나누었을 때 왼쪽 지점에 답이 존재
                    break
            if temp>0:
                left=mid+1 # 이분법으로 나누었을 때 오른쪽 지점에 답이 존재
        return answer

