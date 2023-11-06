# 보석 쇼핑
# 통과는 되나 정확성과 효율성이 떨어짐
import collections

def solution(gems):
    answer = [0, 0]
    k = len(set(gems))

    maxL = 1000000

    for i in range(len(gems)):
        sH = collections.defaultdict(int)
        for j in range(i, len(gems)):
            sH[gems[j]]+= 1
            if len(sH) == k:
                if j - i + 1 < maxL:
                    maxL = j - i + 1
                    answer = [i+1, j+1]
                break

    return answer

#개선 코드
import collections

def solution(gems):
    answer = [0, 0]
    sH = collections.defaultdict(int)

    # 보석의 종류 (중복제거를 하면 보석의 종류가 나오니까!)
    k = len(set(gems))

    lt = 0
    maxL = 10000000

    for rt in range(len(gems)):
        sH[gems[rt]] += 1
        while (len(sH) == k ):
            if rt - lt + 1 < maxL:
                maxL = rt - lt + 1
                answer = [lt+1, rt+1]
            sH[gems[lt]] -= 1
            if sH[gems[lt]] == 0:
                del sH[gems[lt]]
            lt += 1

    return answer