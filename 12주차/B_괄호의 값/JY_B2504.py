# baekjoon 2504 : 괄호의 값
# solved by JY
# DATE : 2021.03.31
# stack, 재귀 이용


import sys
input = sys.stdin.readline
st = str(input().rstrip('\n'))
part = [-1]*len(st) # 내 짝이 몇번째 idx에 있는 지 저장

def check(br):      # 올바른 괄호열인지 확인하는 함수
    stack = []
    for idx, b in enumerate(br):
        if len(stack) == 0:
            if b == ')' or b == ']':
                return False
            stack.append((idx, b))
            continue

        top = stack[-1][1]
        if b == ')':
            if top != '(':
                return False
            p = stack.pop()
            part[p[0]] = idx
        elif b == ']':
            if top != '[':
                return False
            p = stack.pop()
            part[p[0]] = idx
        else:
            stack.append((idx,b))

    if len(stack) != 0:
        return False
    return True


if not check(st):   # 올바르지 못한 문자열인 경우
    print(0)
else:               # 올바른 문자열인 경우
    # sidx와 st[sidx]가 끝나는 eidx
    def rec(sidx, eidx):
        if eidx - sidx == 1:
            return 1
        ret = 0
        sidx += 1
        # 하나의 괄호 안의 괄호들 처리
        while sidx < eidx - 1:  # + 처리
            s_end = part[sidx]  
            if st[sidx] == '(':
                ret += 2 * rec(sidx, s_end)
            else:
                ret += 3 * rec(sidx, s_end)
            sidx = s_end + 1

        return ret

    print(rec(-1, len(st)))
