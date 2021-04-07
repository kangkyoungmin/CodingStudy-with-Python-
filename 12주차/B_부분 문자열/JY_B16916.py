# baekjoon 16916 : 부분 문자열
# solved by JY + hint
# DATE : 2021.04.05
# KMP 알고리즘
# pi[i] = 0~i 까지의 부분 문자열 중에서 prefix == suffix가 될 수 있는 부분 문자열 중에서 가장 긴 것의 길이

import sys
input = sys.stdin.readline
s, p = str(input().strip()), str(input().strip())

def getpi(st):
    length, j = len(st), 0
    pi = [0]*length
    for i in range(1, length):
        while j > 0 and st[i] != st[j]:
            j = pi[j-1]
        if st[i] == st[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(s, p):
    pi = getpi(p)
    plength, j = len(p), 0
    for si in s:
        while j > 0 and si != p[j]:
            j = pi[j-1]
        if si == p[j]:
            if j == plength - 1:    # p가 s의 부분 문자열임
                return 1
            j += 1
    return 0

print(kmp(s, p))