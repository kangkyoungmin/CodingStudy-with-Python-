
# 완주하지 못한 선수의 이름을 리턴하도록 한다
# zip 함수: 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
# zip 함수를 이용하여 각 튜플 순서대로 서로를 묶어 준다
# any 함수: 하나라도 참이 있으면 True를 돌려주고 모두 거짓일 때만 False를 돌려준다
# dir: 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다
# divmod: 2개의 숫자를 입력받고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
def solution(p,c):
    p.sort()
    c.sort()
    
    for par,com in zip(p,c):
        if par!=com:
            return par
    return p[-1]
