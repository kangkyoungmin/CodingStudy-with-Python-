# baekjoon 1920 : 수 찾기
# solved by JY
# DATE : 2020.01.27
# 이분탐색, python3으로 채점

def solution(num, l_idx, r_idx):
  flag = True   # 존재 유무를 확인하는 flag. 존재 시 False
  while l_idx <= r_idx: # left_idx가 right_idx를 넘지 않을때까지 수행
    mid_idx = int((l_idx + r_idx) / 2)
    if num == n_list[mid_idx]:  # n_list에 해당 숫자가 존재
      print(1)  # 숫자가 있으니 1 출력
      flag = False
      break
    elif n_list[mid_idx] < num: # num이 더 크면 left_idx를 조정
      l_idx = mid_idx + 1
    else:                       # num이 더 작으면 right_idx를 조정
      r_idx = mid_idx - 1

  if flag:  # 숫자가 없으면 0 출력
    print(0)

# run test
N = int(input())
n_list = list(map(int, input().split(' ')))
M = int(input())
m_list = list(map(int, input().split(' ')))
n_list.sort()
for i in m_list:
  solution(i, 0, len(n_list) - 1)
