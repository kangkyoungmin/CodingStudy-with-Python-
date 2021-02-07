def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers의 원소는 0이상, 1000이하라는 조건 통해
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
