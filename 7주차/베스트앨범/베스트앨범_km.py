# # 속한 노래가 많이 재생된 장르를 먼저 수록
# # 장르 내에서 많이 재생된 노래를 먼저 수록
# # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
# # 많이 재생된 장르 > 많이 재생된 노래 > 고유 번호가 낮은 순서
# from itertools import groupby

def solution(genres, plays):
    answer = []
    rank=[]
    temp=[]
    values=0
    result=[]
    iter=[]
    # zip 함수를 이용하여 index, genres,plays를 묶어낸다
    for d1,d2,d3 in zip(genres,plays,range(len(plays))):
        temp.append([d1,d2,d3])
        rank.append(d1)
    # # dictionry를 이용하여 간략하게 나타낼 수 있다
    # d={e:[] for e in set(genres)} # genres정보를 담아낸다
    # for e in zip(genres,plays,range(len(genres))):
    #     d[e[0]].append([e[1],e[2]])
    # # 이렇게 나타내면 dictiory를 이용하여 keys, values와 같은 함수를 사용하여 구현할 수 있따
    
    # set(rank)를 통하여 중복되지 않게 고유 순위에 대한 합계를 알아낸다
    for r in set(rank):
        values=0
        for t in temp:
            if t[0]==r:
                values+=t[1]
        result.append([r,values])
    # sort를 통하여 위에서 구한 고유 sum합계별로 sort시키고, zip함수를 통해 묶어낸 것 또한 keys별로 sort시킨다
    result.sort(reverse=True,key=lambda x:x[1])
    temp.sort(reverse=True,key=lambda x:x[1])
    print(temp)
    print(result)
    
    for r in result:
        n=0
        for t in temp:
            if r[0]==t[0] and n<2:
                n+=1
                answer.append(t[2])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))



def solution2(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    print(d)
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    # lambda 함수에 lambda 함수를 사용하여 keys별로 정렬된 데이터에서 keys별 합을 출력해낼 수 있다
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

print(solution2(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))

dic={}
dic['classic']=[[500,0]]
print(dic)
