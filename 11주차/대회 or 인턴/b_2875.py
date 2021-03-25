# 대회 or 인턴

# n 명의 여학생과 M명의 남학생이 팀을 찾는다
# n 2 m 1
# 인턴쉽에 참여하면 대회에 참여하지 못한다

n,m,k=map(int,input().split())

for _ in range(k):
    if 2*m <n:
        n-=1
    else:
        m-=1

print(min(n//2,m))

