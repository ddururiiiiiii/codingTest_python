

# 두 수의 합
def solution1(num1, num2):
    answer = -1

    answer = num1 + num2
    print("두수의 합 : ", answer)
    return answer

# 두 수의 차
def solution2(num1, num2):
    answer = -1

    answer = num1 - num2
    print("두수의 차 : ", answer)
    return answer

# 두 수의 곱
def solution3(num1, num2):
    answer = -1

    answer = num1 * num2
    print("두수의 곱 : ", answer)
    return answer

# 몫 구하기
def solution4(num1, num2):
    answer = -1

    answer = num1 // num2
    print("두수의 몫 : ", answer)
    return answer

def main():
    print("Main Function")
    solution1(3, 4)
    solution2(4, 1)
    solution3(3, 4)
    solution4(10, 4)

if __name__ == "__main__":
    main()


