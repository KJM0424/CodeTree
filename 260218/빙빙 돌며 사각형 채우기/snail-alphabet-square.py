n, m = map(int, input().split())

# Please write your code here.
#(시계방향)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

grid = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y, dir_num = 0, 0, 0
grid[x][y] = 'A'
curr_ascii = 65  #'A'의 아스키코드 값

for _ in range(1, n * m):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    #격자를 벗어나거나 이미 채워져 있으면 90도 회전
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
    x, y = nx, ny
    
    #알파벳 순환 로직: 'Z'(90) 다음은 다시 'A'(65)로
    curr_ascii += 1
    if curr_ascii > 90:
        curr_ascii = 65
        
    grid[x][y] = chr(curr_ascii)

for row in grid:
    print(*row)