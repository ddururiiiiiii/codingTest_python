#개미 군단
def solution(hp):
    answer = 0
    count = 0

    while (hp >= 5):
        hp -= 5
        count += 1

    while (hp >= 3):
        hp -= 3
        count += 1

    while (hp >= 1):
        hp -= 1
        count += 1

    return count

# 모스 부호 (1)
def solution(letter):
    morse = {
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }

    letter = letter.split(' ')

    answer = []

    for i in letter:
        answer.append(morse[i])
    return ''.join(answer)

# 가위 바위 보
def solution(rsp):


    result = {'2':'0','0':'5','5':'2'}

    answer = ''

    for i in rsp:
        answer += result.get(i)
    return answer

# 구슬을 나누는 경우
import math

def solution(balls, share):
    answer = math.factorial(balls) // (math.factorial(balls-share) * math.factorial(share))

    return answer