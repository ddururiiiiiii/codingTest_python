# 최댓값 만들기 (2)
def solution(numbers):
    numbers.sort(reverse = True)
    return max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])

# 캐릭터의 좌표
def solution(keyinput, board):
    limit_x = (board[0] - 1) // 2
    limit_y = (board[1] - 1) // 2

    commands = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0],
    }

    x = y = 0
    for command in keyinput:
        dx, dy = commands[command]
        nx, ny = x + dx, y + dy
        if abs(nx) <= limit_x and abs(ny) <= limit_y:
            x, y = nx, ny

    return [x, y]

# 다항식 더하기
def solution(polynomial):
    answer = '0'
    l = polynomial.split("+ ")
    ans = [0,0]
    for a in l:
        a = a.strip()
        if a[-1] == "x":
            if len(a) == 1:
                ans[0] += 1
            else:
                ans[0] += int(a[:-1])
        else:
            ans[1] += int(a)

    if ans[0] == 0:
        return str(ans[1])
    elif ans[1] == 0:
        if ans[0] == 1:
            return "x"
        return str(ans[0])+"x"
    if ans[0] == 1:
        return "x + " + str(ans[1])
    return str(ans[0])+"x" + " + " + str(ans[1])

# 직사각형 넓이 구하기
def solution(dots):
    w = max(dots)[0] - min(dots)[0]
    h = max(dots)[1] - min(dots)[1]
    area = w*h
    return area