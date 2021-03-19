# programmers L2 : 순위 검색
# solved by JY + hint
# DATE : 2021.03.18
# 이분탐색 사용

import collections
import bisect

store = collections.defaultdict(list)
def div(st):    # st의 모든 경우의 수 구하기(16개) > store에 점수 추가
    l, e, n, f, s = st.split(' ')
    for l1 in [l, '-']:
        for e1 in [e, '-']:
            for n1 in [n, '-']:
                for f1 in [f, '-']:
                    store[l1+' '+e1+' '+n1+' '+f1].append(int(s))

def solution(info, query):
    answer = []    
    for st in info:
        div(st)
    for s in store:     # 점수 정렬
        store[s].sort()
    for q in query:
        l, _, e, _, n, _, f, s = q.split(' ')
        st = l+' '+e+' '+n+' '+f
        idx = bisect.bisect_left(store[st],int(s))  # 점수 위치 이분탐색으로 찾기
        answer.append(len(store[st])-idx)           # 점수 이상인 지원자 수 저장
    return answer

# run test
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]), [1,1,1,1,2,4])
# print(solution())