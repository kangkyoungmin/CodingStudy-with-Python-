# 캠핑
# V를 P로 나눈 몫을 L에 곱해주고, 나머지를 더해준다
i=0
while(1):
    L,P,V=map(int,input().split())
    i+=1
    if L==0 and P==0 and V==0:
        break
    temp=V//P

    result=temp*L+min(L,V%P)
    print('Case '+str(i)+': '+str(result))