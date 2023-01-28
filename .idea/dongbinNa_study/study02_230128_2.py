
# 1이 될 때 까지
n = 25
k = 3
result = 0

while True :
    target = (n // k) * k
    result += n - target
    n = target

    if n < k:
        break
    result += 1
    n // k

result += (n - 1)
print(result)
