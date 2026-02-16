n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# 격자 초기화
grid = [[0] * n for _ in range(n)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for r, c in points:
    x, y = r - 1, c - 1
    
    #해당 칸 색칠하기
    grid[x][y] = 1
    
    #색칠된 칸 개수 세기
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
            
    # 4. 인접한 칸이 정확히 3개면 편안한 상태(1), 아니면 0 출력
    if cnt == 3:
        print(1)
    else:
        print(0)