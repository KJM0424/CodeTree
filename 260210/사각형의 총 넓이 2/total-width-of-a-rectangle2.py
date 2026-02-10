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

for i in range(n):
    #OFFSET을 더해서 인덱스를 0~200 사이로 맞춤
    #직사각형의 넓이는 (x1 ~ x2-1), (y1 ~ y2-1) 까지 칠해야 함
    for x in range(x1[i] + OFFSET, x2[i] + OFFSET):
        for y in range(y1[i] + OFFSET, y2[i] + OFFSET):
            grid[x][y] = 1  

# 칠해진 영역개수 세기
area = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] == 1:
            area += 1

print(area)