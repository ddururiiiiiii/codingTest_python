# 거스름돈
n = 1260
count = 0


# 큰 단위 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array :
    count += n // coin ## 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 1이 될 때까지

# n, k를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True :
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k :
        break
    # k로 나누기
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)