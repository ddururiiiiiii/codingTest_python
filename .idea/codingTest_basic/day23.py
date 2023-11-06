# 특이한 정렬
def solution(numlist, n):
    answer = sorted(numlist, key = lambda x : (abs(x-n), -x))
    return answer

# 등수 매기기
def solution(score):
    answer = []
    val = []

    for i in score:
        val.append(sum(i) / len(i))

    sort = sorted(val, reverse=True)

    for i in val:
        answer.append(sort.index(i)+1)

    return answer

# 옹알이 (1)
import re

def solution(babbling):
    answer = 0
    word = ['aya','ye','woo','ma']

    for b in babbling:
        if any(w*2 in b for w in word):
            continue
        for w in word:
            b = re.sub(f"{w}",' ',b)
        b = re.sub("\ +",'',b)
        if not b:
            answer += 1

    return answer

# 로그인 성공?
def solution(id_pw, db):
    answer = 'fail'
    for id, pw in db:
        if id_pw[0] == id:
            if id_pw[1] == pw:
                answer = 'login'
            else:
                answer = 'wrong pw'
    return answer