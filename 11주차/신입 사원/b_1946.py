# 신입 사원

n=int(input())
for i in range(n):
    test_case=int(input())
    temp=[0] * test_case
    cnt=0

    for j in range(test_case):
        first,second=map(int,input().split())
        temp[first-1]=second
    temp2=temp[0]

    for k in range(1,test_case): # 서류 성적 기준으로 오름 차순 되었음 
        if temp2<temp[k]: # 면접 등수가 더 높을 때 cnt+1
            cnt+=1
        else:
            temp2=temp[k] # 면접 등수가 더 낮으면 해당 등수로 갱신한다
             

    # for i in range(len(temp)):
    #     for j in range(len(temp)):
    #         if i==j:
    #             continue
    #         if temp[j][0]<temp[i][0] and temp[j][1]<temp[i][1]:
    #             cnt+=1
    #             break
    
        
    print(test_case-cnt)

