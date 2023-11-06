# 점의 위치 구하기
def solution(dot):
    answer = 0

    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        else :
            answer = 4
    else :
        if dot[1] > 0:
            answer = 2
        else :
            answer = 3

    return answer

# 2차원으로 만들기
import numpy as np

def solution(num_list, n):
    answer = np.array(num_list).reshape(-1, n)
    return answer.tolist()

# 공 던지기
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

# 배열 회전 시키기
from collections import deque

def solution(numbers, direction):

    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    elif direction == "left":
        numbers.rotate(-1)

    return list(numbers)