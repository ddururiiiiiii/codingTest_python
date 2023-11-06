# 단속 카메라
def solution(routes):
    answer = 1

    # 나가는 지점에서 오름차순 정렬
    routes.sort(key = lambda x : x[1])

    point = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > point:
            point = routes[i][1]
            answer += 1

    return answer