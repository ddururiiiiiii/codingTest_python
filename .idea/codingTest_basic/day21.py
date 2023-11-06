# 삼각형의 완성조건 (2)
def solution(sides):
    return (sorted(sides)[0] * 2) - 1

# 외계어 사전
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

# 숨어있는 숫자의 덧셈 (2)
import re
def solution(my_string):
    return sum(map(int,re.findall(r"[0-9]+",my_string)))

# 안전지대
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)