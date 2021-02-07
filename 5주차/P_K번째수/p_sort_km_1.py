# k번째 수

# array=[1,5,2,6,3,7,4], i=2,j=5,k=3

def solution(array,commands):
    answer=[]

    for k in commands:
        temp=array[(k[0]-1):k[1]]
        temp.sort()
        answer.append(temp[k[2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))