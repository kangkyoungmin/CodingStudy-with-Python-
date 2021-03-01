# programmers L2 : 전화번호 목록
# solved by JY
# DATE : 2021.02.28
# dictionary 사용. sort사용보다 빠름

def solution(phone_book):
    dic = {}
    for phone in phone_book:
        dic[phone] = 1

    for phone in phone_book:
        tmp = ""
        for num in phone:
            tmp += num
            if tmp in dic and tmp != phone:
                return False

    return True

# run test
print(solution(["119", "97674223", "1185524421", "118"]))  # false