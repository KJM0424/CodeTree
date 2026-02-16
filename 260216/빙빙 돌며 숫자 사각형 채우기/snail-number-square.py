n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

next_dir = [3, 2, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

x, y = 0, 0
dir_num = 3  # 처음 시작 방향은 오른쪽 3

arr[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = next_dir[dir_num]  # 리 만들어둔 매핑 배열로 방향 꺾기
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
    x, y = nx, ny
    arr[x][y] = i

for row in arr:
    print(*row)