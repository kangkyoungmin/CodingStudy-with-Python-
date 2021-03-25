# 한 개의 회의실이 있따
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의이 최대 개수
# 시작시간과 끝나는 시간이 주어져 있다
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수는?

# sol
# 시작시간은 끝나는 시간보다 큰 것 중에 최소값
# 끝나는 시간은 그냥 최솟값인 것

n=int(input())
room=[]
for i in range(n):
    room.append(list(map(int,input().split())))
temp2=sorted(room,key=lambda x:[x[1],x[0]])

cnt=1
s,e=temp2[0][0],temp2[0][1]
for start,end in temp2[1:]:
    if start>=e:
        e=end
        cnt+=1
print(cnt)
    





