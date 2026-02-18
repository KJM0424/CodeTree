n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

if k <= n:
    x, y, dir_num = 0, k - 1, 0
elif k <= 2 * n:
    x, y, dir_num = k - n - 1, n - 1, 1
elif k <= 3 * n:
    x, y, dir_num = n - 1, n - (k - 2 * n), 2
else:
    x, y, dir_num = n - (k - 3 * n), 0, 3


reflect_slash = [1, 0, 3, 2]

reflect_backslash = [3, 2, 1, 0]

ans = 0

#레이저가 격자를 벗어날 때까지 시뮬레이션
while 0 <= x < n and 0 <= y < n:
    ans += 1  #격자 안의 모든 칸에는 거울이 있으므로 밟을 때마다 1번씩 튕김
    
    #거울 모양에 따라 방향 전환
    if grid[x][y] == '/':
        dir_num = reflect_slash[dir_num]
    else: 
        dir_num = reflect_backslash[dir_num]
        
    #튕겨진 방향으로 이동
    x += dxs[dir_num]
    y += dys[dir_num]

print(ans)