# DFS 소스코드 예제

# def 메서드 정의
def dfs(gragh, v, vistited):
    # 현재 노드를 방문 처리
    vistited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노트를 재귀적으로 방문
    for i in gragh[v]:
        if not vistited[i]:
            dfs(gragh, i, vistited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)