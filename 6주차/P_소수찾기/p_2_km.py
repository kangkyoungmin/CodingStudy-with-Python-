# 완전 탐색 소수 찾기

# 한자리 숫자가 적힌 종이 조각
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 한다

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 
# 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요

# numbers는 길이 1이상 7이하인 문자열
# 0~9까지 숫자만으로 이루어짐
# 조합을 어떻게 할 수 있는지,소수인지 아닌지에 대한 검증
# 조합 구하는 법
# 소수: 1과 자기자신을 제외하고는 나누어 떨어지지 않는다

from itertools import combinations
from itertools import permutations
def solution(numbers):

    def sosu(num):
        if num<=1: return False
        for k in range(2,num):
            if num%k==0:
                return False
        return True

    num_list=[]
    n_list=[]
    midium_list=[]
    for n in numbers:
        num_list.append(n)
        n_list.append(n)
    for i in range(2,len(num_list)+1):
        n_list.append(list(permutations(num_list,i)))
    # 길이를 이용하여 해당 길이만큼 리스트에 있는 값을 붙여준다
    for n in n_list:
        # 한 자릿 수일 경우는 그냥 리스트에 넣어준다
        if len(n)==1:
            if sosu(int(n))==True:
                midium_list.append(int(n))
        else:
        # 두 자릿 수 이상일 경우 해당 문자열을 더하여 넣어준다
            for j in range(len(n)):
                r_num=''
                for m in n[j]:
                    r_num+=m
                if sosu(int(r_num))==True:
                    midium_list.append(int(r_num))
    return len(set(midium_list))

        
        



print(solution("17"))
