# 간단한 논리연산
def solution(x1, x2, x3, x4):
    return ((x1 or x2) and (x3 or x4))

# 주사위 게임3
def solution(a, b, c, d):

    # set : 중복과 순서가 없음.
    nums = {a, b, c, d};

    # 네 주사위에 적힌 숫자가 모두 다르다면 최소값 return
    if len(nums) == 4:
        return min(nums)

    # 딕셔너리 : key, value 형태
    # 주사위의 값이 몇번 나왔는지 딕셔너리 형태 정리
    count = {}
    for num in (a, b, c, d):
        count[num] = count.get(num, 0) + 1

    # 네 주사위에서 나온 숫자가 모두 같을 때
    if len(nums) == 1:
        return nums.pop() * 1111

    # 네 주사위의 나온 숫자가 2개 이면서
    elif len(nums) == 2:
        if 3 in count.values(): # value 값이 3인 것
            p = [k for k, v in count.items() if v == 3][0]
            q = [k for k in nums if k != p][0]
            return (10 * p + q) ** 2
        else:
            p, q = count.keys()
            return (p + q) * abs(p - q)
    else:
        p = [k for k, v in count.items() if v == 2][0]
        q, r = [k for k in nums if k != p]
        return q * r



# 글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    answer = ''

    for i in range(len(index_list)):
        answer += my_string[index_list[i]]

    return answer

# 9로 나눈 나머지
def solution(number):
    answer = 0
    sum = 0
    if int(number) >= 0 :
        for i in number:
            sum += int(i)

    answer = sum % 9
    return answer

# 문자열 여러 번 뒤집기
def solution(my_string, queries):
    for start, end in queries:
        my_string = my_string[:start] + my_string[start:end+1][::-1] + my_string[end+1:]
    return my_string