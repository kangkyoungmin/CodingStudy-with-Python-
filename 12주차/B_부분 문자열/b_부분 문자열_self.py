# pi배열을 만드는 함수
# 이렇게 kmp 알고리즘은 틀렸다는 사실이 아니라 조금이라도 일치했었다는 정보에 주목하고 미리 전처리 해둔 pi배열을 이용해서 많은 중간 시도를 껑충 건너띌 수 있게 합니다.


# 접두사와 접미사가 같은 것을 찾아내는 게 포인트
def make_table():
    table=[0]*len(P) # 문자열의 실패를 경험 삼은 패턴 수
    j=0 # 이전의 성공 정보를 저장

    for i in range(1,len(P)): # 1부터 시작해야 한다 0부터는 의미 x
        while j>0 and P[i]!=P[j]: # 문자열이 같지 않을 떄
            j=table[j-1] # 이전까지 같았던 문자의 개수로 만들어준다
        if P[i]==P[j]: # 문자열이 같을 때
            j+=1
            table[i]=j
    return table
    # 이것의 의미를 보면 ABAB 라는 패턴이 있을 때 p[2]의 경우 앞서 두 경우를 비교하지 않아도 이미 포함되어 있다고 생각한다
    # ABCDAB가 있다면 실패의 경험을 삼아 P[5]=2,라고 할 수 있다. 
    # 문자열 안에서 시작했을 떄 몇 개를 생략할 수 있는지에 대한 정보를 TABLE에 심어준다

def KMP():
    table=make_table()
    j=0
    
    for i in range(0,len(S)):
        while j>0 and S[i]!=P[j]:
            j=table[j-1]
        if S[i]==P[j]: # 문자열이 같을 때 
            if j==len(P)-1:
                return True
            else:
                j+=1
        
    


S=input()
P=input()

if KMP():
    print(1)
else:
    print(0)