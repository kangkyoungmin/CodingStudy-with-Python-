from collections import Counter
n,m=map(int,input().split())

s_Arr=[]
s_list=[]
count=[0]*n
tmp=['']*m
for i in range(n):
    temp=input()
    s_Arr.append(temp)
    s_list.append(list(temp))

for i in range(0,m):
    for s in s_list:
        tmp[i]+=s[i]

result=''

for t in tmp:
    temp=Counter(t).most_common()

    temp.sort(key=lambda x:[-x[1],x[0]])


    for t2 in temp:
        result+=t2[0]
        break

print(result)
answer=0
for s in s_Arr:
    cnt=0
    for i in range(0,m):
        if result[i]!=s[i]:
            cnt+=1
    answer+=cnt
print(answer)
        




