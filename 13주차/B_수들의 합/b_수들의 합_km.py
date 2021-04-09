# 수들의 합
# 서로 다른 N개의 자연수의 합이 s라고 한다
# 자연수 N의 최댓값은?
import math
n=int(input())

k=(-1+math.sqrt(1+8*n))//2
print(int(k))