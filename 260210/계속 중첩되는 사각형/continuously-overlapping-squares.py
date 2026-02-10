n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
OFFSET = 100
MAX_R = 200
grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

#사각형 순서대로 칠하기
for i in range(n):
    # 짝수 인덱스 빨간색, 홀수 파란색
    if i % 2 == 0:
        color = 1  
    else:
        color = 2  
    
    rect_x1 = x1[i] + OFFSET
    rect_y1 = y1[i] + OFFSET
    rect_x2 = x2[i] + OFFSET
    rect_y2 = y2[i] + OFFSET
    
    #색깔 덮어쓰기
    for x in range(rect_x1, rect_x2):
        for y in range(rect_y1, rect_y2):
            grid[x][y] = color

#파란색 영역넓이 
blue_area = 0
for row in grid:
    blue_area += row.count(2)

print(blue_area)