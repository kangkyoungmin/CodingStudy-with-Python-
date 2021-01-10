#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(n, lost, reserve):

    lost2 = set(lost) - set(reserve)

    reserve2 = set(reserve) - set(lost)

    for i in lost2:

        if i + 1 in reserve2:

            reserve2.remove(i + 1)

        elif i - 1 in reserve2:

            reserve2.remove(i - 1)

        else:

            n-=1

    return n



#set : 중복값X, 순서X(인덱스불가), 차집합 가능

#튜플 : 리스트와 비슷, 수정불가

#리스트 : 수정가능, 중복가능, 순서O(인덱스가능)

#딕셔너리 : 키:값, 수정불가, 중복불가, 순서X

