def solution(phone_book):

    phone_book.sort()
    for data in phone_book:
        temp=len(data)
        for data2 in phone_book:
            if data==data2: continue 
            if data[:temp] in data2[:temp]: # 접두어가 아닌 경우도 패스한다
                return False
            else:
                continue
            
    return True

print(solution(["1195524421","119"]))
print(solution(["123","456","789"]))

# 솔루션 풀이
# startswith()은 내가 찾고자 하는 문자열A가 문자열B의 맨 앞에 있는지의 여부를 알려준다
def solution2(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book = [12,23,22,17] # phone_book[1:] = [23,22]

for p1, p2 in zip(phone_book, phone_book[1:]) :
	print(p1,p2)  

# 문자열로 sort를 하게 되면 배열의 첫 번째 원소부터 비교하게 된다
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

print(solution(["123","456","45"]))
