# programmers L2 : 전화번호 목록
# solved by JY
# DATE : 2021.02.28
# sort 사용

def solution(phone_book):
    phone_book.sort()

    for idx in range(1, len(phone_book)):
        if len(phone_book[idx-1]) > len(phone_book[idx]):
            continue
        if phone_book[idx - 1] == phone_book[idx][:len(phone_book[idx-1])]:
            return False

    return True

# run test
print(solution(["119", "97674223", "1185524421", "118"]))  # false