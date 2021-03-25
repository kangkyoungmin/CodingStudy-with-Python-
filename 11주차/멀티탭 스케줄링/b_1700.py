# 멀티탭 문제
# 멀티탭을 뺴는 횟수를 최소화해야 한다
# 일단 스택으로 접근하는 게 좋을 듯하다

# 뺴는 순서를 어떻게 정해야 하는가?
# 새로 더해야 하는 것을 건너 뛰고 그 다음부터 돌면서
# 리스트에 있는 것이 있다면 count, count가 len(list)-1이면 종료
# 만약 나오지 않으면 제일 마지막 것을 뺀다
# 더 자주 쓰인 것이 우선순위 1, 그 

# 구멍의 개수와 사용횟수
n,m=map(int,input().split())

tab=list(map(int,input().split()))

multi=[]
answer=0

for i in range(0,len(tab)):
    if tab[i] in multi: # 꽂혀있으면 넘긴다
        continue
    if len(multi)<n: # 비어있으면 꽂는다
        multi.append(tab[i])
    elif len(multi)==n: # 풀로 차 있을 경우
        temp=set()
        for t in tab[i+1:]: # 그 다음부터 쭉 돌면서 multi에 있는 것을 찾는다
            if t in multi:
                temp.add(t)

        if len(set(temp))==len(multi): # 만약 뒤에 멀티탭에 있는 모든 것들이 있을 경우
            multi.remove(list(temp)[-1])
        else: # 안 쓰이는 것들을 하나뺴준다
            temp2=list(set(multi)-set(temp))
            multi.remove(temp2[-1])
        multi.append(tab[i])
        answer+=1
    
print(answer)

# a=[1,1,2,2,2]
# print(a.count(2))






