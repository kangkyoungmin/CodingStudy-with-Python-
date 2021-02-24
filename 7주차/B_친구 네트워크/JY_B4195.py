# baekjoon 4195 : 친구 네트워크
# solved by JY
# DATE : 2021.02.23
# dic : { name : 그룹번호=friend의 idx 번호 }
# friend : [ {set으로 구성. name들의 모임}, 숫자인 경우 friend의 idx, ....]

# run test
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    F = int(input())
    dic, friend = {}, []
    for _ in range(F):
        f1, f2 = map(''.join, input().rstrip('\n').split(" "))

        if f1 not in dic and f2 not in dic:     # 서로 첫 친구일 때
            friend.append(set([f1, f2]))        # 새 그룹 생성
            dic[f1] = dic[f2] = len(friend) - 1
            ans = 2
        elif f1 in dic and f2 in dic:
            while type(friend[dic[f1]]) == int:     # int > 부모를 찾아 가야함. 
                dic[f1] = friend[dic[f1]]
            while type(friend[dic[f2]]) == int:     # int > 부모를 찾아 가야함. 
                dic[f2] = friend[dic[f2]]
            
            if dic[f1] != dic[f2]:  # 다른 그룹일 경우 Union
                if len(friend[dic[f1]]) < len(friend[dic[f2]]): # 더 작은 그룹을 합치기
                    friend[dic[f2]] |= friend[dic[f1]]
                    friend[dic[f1]] = dic[f2]
                    ans = len(friend[dic[f2]])
                else:
                    friend[dic[f1]] |= friend[dic[f2]]
                    friend[dic[f2]] = dic[f1]
                    ans = len(friend[dic[f1]])
            else:
                ans = len(friend[dic[f1]])

        elif f1 not in dic and f2 in dic:
            while type(friend[dic[f2]]) == int:     # int > 부모를 찾아 가야함. 
                dic[f2] = friend[dic[f2]]
            friend[dic[f2]].add(f1)
            dic[f1] = dic[f2]
            ans = len(friend[dic[f1]])
        elif f1 in dic and f2 not in dic:
            while type(friend[dic[f1]]) == int:     # int > 부모를 찾아 가야함. 
                dic[f1] = friend[dic[f1]]
            friend[dic[f1]].add(f2)
            dic[f2] = dic[f1]
            ans = len(friend[dic[f1]])

        print(ans)
        