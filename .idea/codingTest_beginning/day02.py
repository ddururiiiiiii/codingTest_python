# 덧셈식 출력하기
a, b = map(int, input().strip().split(' '))
print(str(a)+" + " + str(b) + " = " + str(a+b))
# print(f"{a} + {b} = {a + b}")

# 문자열 붙여서 출력하기
str1, str2 = input().strip().split(' ')
print(str(str1) +  str(str2))
# print(input().strip().replace(' ', ''))

# 문자열 돌리기
str = input()
for i in str :
    print(i)

# print('\n'.join(input()))

# 홀짝 구분하기
a = int(input())

if a%2 == 0 :
    print(str(a) + " is even")
else :
    print(str(a) + " is odd")


# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]