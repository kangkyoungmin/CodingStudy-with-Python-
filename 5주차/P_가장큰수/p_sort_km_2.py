# 가장 큰 수
# 정수를 이어 붙여 만들 수 있는 가장 큰 수?

# 최고차항을 알아내고 그에 맞게 수를 개편한다
# 정렬하면 끝이다

# solution
# def solution(numbers):
#     answer = []
#     cnt=[]
#     result=[]
#     rresult=""
#     for n in numbers:
#         count=0
#         while(n>=1):
#             n=n//10
#             if n>=1:
#                 count+=1
#         cnt.append(count)
#     mcount=max(cnt)
#     numbers=list(map(str,numbers))

#     for n in numbers:  
#         for _ in range(mcount-len(n)+1):
#             n+=n[-1]
#         answer.append(n)

#     for i,data in enumerate(answer):
#         result.append((i,data))
    
#     result=sorted(result,key=lambda x:x[1],reverse=True)
    
#     for r in result:
#         rresult+=numbers[r[0]]
#     return rresult

# print(solution([0, 0, 0]))

def solution(num):
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    return str(int(''.join(num)))




def partition(nums,l,r):
    # print(nums,l,r)
    low=1
    while l<r:
        # l+r>r+l
        if compare(num[l],nums[r]):
            nums[l],nums[low]=nums[low],nums[l]
            low+=1
        
        l+=1
    
    nums[low],nums[r]=nums[r],nums[low]
    return low

def myQuickSort(nums,l,r):
    # 왼쪽이 더 크면 종료
    if l>=r:
        return
    # pos를 진행하면서  L에서 r까지의 범위가 정렬이 됨(우선순위 가장 작은 게 맨 뒤에 감)
    # pos는 nums에서 가장 우선순위가 작은 값
    pos=partition(nums,l,r)

    # QuickSort는 pos(우선순위가 가장 작은 값)
    myQuickSort(nums,l,pos-1)
    myQuickSort(nums,pos+1,r)



