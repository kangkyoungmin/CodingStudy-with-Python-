# programmers L3 : 베스트앨범
# solved by JY
# DATE : 2021.03.01
# dictionary, sorted 사용
# genre = { '장르' : [ [idx1, plays] , [idx2, plays] , ..] }
# g_sum = { '장르' : 합계 }

def solution(genres, plays):
    answer = []
    genre, g_sum = {}, {}

    for idx, g in enumerate(genres):
        if g in genre:
            genre[g].append([idx, plays[idx]])
            g_sum[g] += plays[idx]
        else:
            genre[g] = [[idx, plays[idx]]]
            g_sum[g] = plays[idx]

    s_sum = sorted(g_sum.items(), key=(lambda x: x[1]), reverse=True)   # 조건 1

    for s in s_sum:
        get = genre[s[0]]
        g_hap = sorted(get, key=(lambda x: x[1]), reverse=True) # 조건 2

        answer.append(g_hap[0][0])
        if len(g_hap) > 1:
            answer.append(g_hap[1][0])

    return answer


# run test
print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
