n, m = map(int, input().split())

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

grid = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

#아래 방향으로 시작
x, y = 0, 0
dir_num = 0
grid[x][y] = 1

#2부터 N*M까지 숫자 채우기
for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    #격자를 벗어나거나 이미 숫자가 채워져 있다면
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        #반시계 방향으로 90도 회전
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
    x, y = nx, ny
    grid[x][y] = i

for row in grid:
    print(*row)