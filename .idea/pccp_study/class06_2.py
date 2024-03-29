# 송아지 찾기 - 더 빠른 버전
from collections import deque

def solution(s, e):
    answer = 0
    ch = [0] * 10001
    dQ = deque()
    dQ.append(s)
    ch[s] = 1
    L = 0
    while (dQ):
        length = len(dQ)
        for _ in range(length):
            x = dQ.popleft()
            for nx in [x-1, x+1, x+5]:
                if nx == e:
                    return L + 1
                if nx > 0 and nx <= 10000 and ch[nx] == 0:
                    ch[nx] = 1
                    dQ.append(nx)
        L += 1

    return answer