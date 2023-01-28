
# 거스름 돈 구하기
n = 1250
result = 0

array = [1000, 500, 50, 10]

for coin in array:
    result += n // coin
    n = n % coin

print(result)