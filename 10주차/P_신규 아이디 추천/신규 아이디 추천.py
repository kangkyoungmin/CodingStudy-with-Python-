# 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서
# 규칙에 맞는 아이디를 추천해주는 프로그램을 개발

# 아이디의 길이 : 3~15
# 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 문자만 사용 가능
# 마침표는 처음과 끝에 사용할 수 없음, 연속으로 사용 불가
import re
def solution(new_id):
    # 대문자를 소문자로 치환
    new_id=new_id.lower()
    phase_2=['-','_','.']

    # 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제거
    for i,id in enumerate(new_id):
        if id.isdigit()==True or id in phase_2 or ord('a')<=ord(id)<=ord('z'): # 숫자,뺴기 밑줄 마침표
            continue
        new_id=new_id.replace(id,"") # 이외의 문자들을 제거한다
        # new_id=new_id.replace("..",".") # ..은 .으로 대체한다
    # new_id=new_id.replace("..",".") # 혹시 모를 상황 대비
    new_id=re.sub('\.{2,}','.',new_id) # .이 두 번 이상 반복되는 것을 . 하나로 대체
    new_id=new_id.strip(".") # 문자열 양 끝에 있는 . 제거

    # 문자열이 공백일 때
    if new_id=="":
        new_id="a"
    # 문자열 길이가 16보다 클 때
    if len(new_id)>=16:
        new_id=new_id[:15]
    # 문자열 길이 자르고 나서 앞뒤로 .을 제거해준다
    new_id=new_id.strip(".")
    if len(new_id)<=2:
        while True:
            if len(new_id)==3:
                break
            new_id+=new_id[-1]

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))