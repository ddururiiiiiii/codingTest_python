# 주차 요금 계산

import math

def solution(fees, records):
    answer = []

    # 차량마다 입출차 시간을 기록 하기 위한 배열
    inTime = [0] * 10000

    # 차량마다 입출차 여부를 기록하기 위한 배열
    inIn = [0] * 10000

    # 차량마다 주차시간을 기록하기 위한 배열
    sumT = [0] * 10000

    for record in records:

        # 주차시간, 차량번호, 입출차여부를 쪼갠다
        a, b, c = record.split()

        # 주차시간 계산을 위해 시, 분을 쪼갠다
        h, m = a.split(':')

        # 차량이 입차했을 때
        if c == 'IN':
            # 입차시간을 분으로 환산하여 기록
            inTime[int(b)] = int(h) * 60 + int(m)

            # 입차여부를 기록
            inIn[int(b)] = 1

        # 차량이 출차 했을 때
        else:
            # (출차시간 - 입차시간)을 계산하여 주차시간을 기록
            sumT[int(b)] += (int(h) * 60 + int(m) - inTime[int(b)])


        for i in range(10000):
            if inIn[i] == 1:
                # 출차된 기록이 없을 때 23:59로 출차하여 주차요금 계산
                sumT[i] += (23*60+59) - inTime[i]


        for i in range(10000):
            # 주차기록이 있는 차량만 주차요금 계산하여 배열에 담는다.
            if sumT[i] > 0:
                answer.append(fees[1] + max(math.ceil((sumT[i]  - fees[0]) / fees[2]), 0) * fees[3])
    return answer