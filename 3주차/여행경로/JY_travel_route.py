# programmers L3 : 여행 경로
# solved by JY
# DATE : 2021.02.07
# DFS/BFS

def solution(tickets):
    answer, dic = [], {}
    for t in tickets:
        if t[0] in dic:
            dic[t[0]].append(t[1])
        else:
            dic[t[0]] = [t[1]]

    for d in dic:
        dic[d].sort()
    
    def dfs(key):
        answer.append(key)  # 경로에 추가

        if key in dic and len(dic[key]) != 0:
            for idx, value in enumerate(dic[key]):
                dic[key].pop(idx)               # ticket 제거
                check = dfs(value)
                if check == False:              # 경로 불가
                    dic[key].insert(idx, value) # ticket 다시 추가
                    answer.pop(-1)              # 경로에서 제거

        return True if len(answer) == len(tickets) + 1 else False   # 모든 티켓 사용 시 True

    dfs("ICN")

    return answer

# run test
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])) # ["ICN", "B", "ICN", "A"]
# print(solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']])) # ['ICN', 'B', 'ICN', 'A', 'D', 'A']