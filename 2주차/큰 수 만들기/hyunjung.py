# programmers L2 : 큰 수 만들기
# DATE : 2020.01.13
# Greedy 알고리즘


# * 입력순서유지
# 1. 스택. 리스트에 있는 숫자들을 순서대로 스택에 삽입
# 2. 넣으려는 값이 stack의 마지막 값보다 크면, 기존의 값 삭제 후 새로운 값으로
# 3. 스택 가장 위에 있는 숫자 pop
# 4. pop할때 k-=1

def solution(number, k):
    # stack에 입력값을 순서대로 삽입
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈
        # len(stack) > 0 == stack
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k-1
            stack.pop()
            k -= 1
        # 새로운 값을 삽입
        stack.append(num)
    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이미 큰 수부터 앞에서 채워넣었기 때문
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
