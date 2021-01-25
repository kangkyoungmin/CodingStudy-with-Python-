# 트리를 하나 만들어서 그 수를 뺀 수, 더한 수를 각각 노드로 만들어 붙여
# 최종 트리에서 target의 개수 세기
def solution(numbers, target):
    answer_tree = [0] # 첫 수부터 빼는 경우 있을 수 있어 0 담고 시작/ 이전 수에 대한 계산 결과 담음
    for num in numbers: # 매개변수로 받은 숫자 목록을 하나씩 꺼냄
        sub_tree = [] # 현재 숫자에 대한 결과를 담은 자식노드 하나씩 추가
        for tree_number in answer_tree:  # 노드 하나하나에 숫자를 더하고 빼서 자식 노드 생성
            sub_tree.append(tree_number+num)
            sub_tree.append(tree_number-num)
        answer_tree = sub_tree
    answer = answer_tree.count(target)
    return answer

print(solution([1,1,1,1,1], 3))
