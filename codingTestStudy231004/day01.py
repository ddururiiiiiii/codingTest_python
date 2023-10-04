# 문자열 출력하기
str = input()
print(str)

# a와 b출력하기
a, b = map(int, input().strip().split(' '))
print('a =', a)
print('b =', b)

# 문자열 반복해서 출력하기
a, b = input().strip().split(" ")
for i in range(int(b)):
    print(a, end = "")

# 대소문자 바꿔서 출력하기
str = input().swapcase()
print(str)

# 특수문자 출력하기
print(r'!@#$%^&*(\'"<>?:;')
print("!@#$%^&*(\\'\"<>?:;")