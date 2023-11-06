# 피자 나눠 먹기 (1)
def solution1(n):
    answer = 0

    if ( n % 7 ) == 0 :
        answer = n // 7
    elif ( n % 7 ) != 0 :
        answer = (n // 7 ) + 1

    return answer

# 피자 나눠 먹기 (2)
def solution2(n):
    answer = 0
    pizzaBox = 6

    while pizzaBox % n != 0 :
        pizzaBox += 6

    answer = pizzaBox / 6;

    return answer

# 피자 나눠 먹기 (3)
def solution3(slice, n):
    answer = 0

    if n % slice == 0 :
        answer = n / slice
    else :
        answer = 1 + (n // slice)

    return answer

# 배열의 평균값
def solution4(numbers):

    return sum(numbers) / len(numbers)




