x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
OFFSET = 1000
MAX_R = 2000
grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

#첫번째 직사각형
for x in range(x1[0] + OFFSET, x2[0] + OFFSET):
    for y in range(y1[0] + OFFSET, y2[0] + OFFSET):
        grid[x][y] = 1

#두번째 직사각형 영역 지우기 
#두번째 직사각형이 덮는 부분은 0으로
for x in range(x1[1] + OFFSET, x2[1] + OFFSET):
    for y in range(y1[1] + OFFSET, y2[1] + OFFSET):
        grid[x][y] = 0

#잔해물(1)을 덮는 범위 찾기
min_x, max_x = MAX_R + 1, 0
min_y, max_y = MAX_R + 1, 0
has_debris = False  # 잔해물이 아예 없는 경우

for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if grid[x][y] == 1:
            has_debris = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

#넓이 계산 
if has_debris:
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(width * height)
else:
    print(0)