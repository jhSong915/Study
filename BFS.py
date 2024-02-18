#시작 지점이 2, 종점이 3인 미로를 종점까지의 거리 탐색하는 코드
def bfs(a, b):
    visited = [[0] * N for _ in range(N)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 상하좌우
    queue = []
    queue.append([a, b])  # 큐에 초기값 지정
    visited[a][b] = 1  # 초기값 1
    while queue:
        y, x = queue.pop(0)
        if maze[y][x] == 3:
            return visited[y][x] - 2  # 도착지점 기준 시작값 1과 끝값 1을 뺌
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            # 범위 밖을 벗어남 X, 1이 아님, 방문X
            if 0 <= ny < N and 0 <= nx < N and maze[ny][nx] != 1 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])
    return 0
# 미로 칸 수 설정
N = 5
# 미로 경로 설정
maze = [[2,1,1,1,1],
            [0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,1,1],
            [1,1,0,0,3]]
print(bfs(0,0))