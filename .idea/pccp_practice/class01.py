import collections

def solution(id_list, report, k):
    answer = []

    # 중복 제거
    report = list(set(report))

    # 신고한사람 : 신고당한사람
    reportHash = collections.defaultdict(set)

    # 신고당한사람 : 신고당한횟수
    stopped = collections.defaultdict(int)

    for i in report:
        a, b = i.split(' ')
        reportHash[a].add(b)
        stopped[b] += 1

    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stopped[user] >= k:
                mail += 1
        answer.append(mail)

    return answer






    return answer