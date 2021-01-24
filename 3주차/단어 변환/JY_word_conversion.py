# programmers L3 : 단어 변환
# solved by JY
# DATE : 2020.01.22
# DFS 이용

def check(begin, word):
    count = 0
    for i in range(len(begin)):
        if begin[i] != word[i]:
            count += 1
        if count > 1:
            break

    return True if count == 1 else False

def dfs(begin, target, words):
    if begin == target:
        return 0

    mymin = 0
    for word in words:
        if check(begin, word) == 1:
            ret = dfs(word, target, [data for data in words if data != word]) + 1
            mymin = ret if mymin == 0 else min(mymin, ret)

    return mymin

def solution(begin, target, words):
    return 0 if target not in words else dfs(begin, target, words)

# run test
print(solution("hit", "cog", ["dog", "dot", "hot", "lot", "log", "cog"]))   # 4
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0