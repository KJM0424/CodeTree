n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
OFFSET = 100
MAX_R = 200  # 격자 크기 임의

#격자초기화 
grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for i in range(n):
    # 색종이 크기가 8x8, x ~ x+8, y ~ y+8 칠하면 됨
    
    start_x = x[i] + OFFSET
    start_y = y[i] + OFFSET
    
    for r in range(start_x, start_x + 8):
        for c in range(start_y, start_y + 8):
            grid[r][c] = 1

#칠해진 영역 넓이 구하기
area = 0
for row in grid:
    area += sum(row)

print(area)