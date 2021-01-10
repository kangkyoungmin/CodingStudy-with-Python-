# 1. 상하 : 문자이동
#    1-1. A~14번째 : up
#    1-2. 15번째 ~ Z : down (뒤로 가는 것이 더 최소)
# 2. 좌우 : 위치이동
#     이름에 A가 존재한다면 오른쪽으로 갈건지 왼쪽으로 갈건지 결정해야 함
#     좌우로 움직이는 것은 'A'를 만나면 알파벳을 바꾸지 않아도 되므로 오른쪽에 'A'가 아닌 곳에 더 빨리 만나는 쪽을 찾으면 됨
#     따라서 반복문을 사용해서 왼쪽, 오른쪽으로 갈 경우 'A'가 아닌 문자가 언제 나오는지를 찾고, 더 작은 값을 사용


def solution(name):
    answer = 0
    name = list(name)
    index = 0
    while(True):
        right = 1
        left = 1
        if name[index] != 'A': #1번
            updown = min(ord(name[index])-ord('A'),(ord('Z')-ord(name[index])+1))
            answer += updown
        name[index] = 'A'
        if name == ["A"]*len(name): break
        for i in range(1,len(name)):
            if name[index+i] == "A": right += 1
            else: break
        for i in range(1,len(name)):
            if name[index-i] == "A": left += 1
            else: break
        if right>left:
            answer += left
            index -= left
        else:
            answer += right
            index += right
    return answer
