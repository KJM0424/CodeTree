n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

#정중앙 위치 계산
x, y = n // 2, n // 2
grid[x][y] = 1

num = 2
dir_num = 0
move_len = 1  #직진하는 거리

while num <= n * n:
    # 2방향을 같은 거리만큼 이동 후 거리를 1 증가시킴
    for _ in range(2):
        for _ in range(move_len):
            x += dxs[dir_num]
            y += dys[dir_num]
            grid[x][y] = num
            num += 1
            
            #끝까지 다 채웠으면 모든 반복문 탈출
            if num > n * n:
                break
                
        dir_num = (dir_num + 1) % 4
        
        if num > n * n:
            break
            
    move_len += 1  #2번 꺾었으므로 다음 이동 거리 1 증가

for row in grid:
    print(*row)