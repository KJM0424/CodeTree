R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
cnt = 0

#첫 번째 점프할 위치  고정
#R-1, C-1 까지 탐색
for i in range(1, R - 1):
    for j in range(1, C - 1):
        #항상 현재 위치(i, j)보다 오른쪽 아래로만 가야 함
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                #모두 색이 달라야 함
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[R-1][C-1]:
                    cnt += 1

print(cnt)