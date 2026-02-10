x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

OFFSET = 1000
MAX_R = 2000  #최대 크기 (2000 x 2000)

# 초기화
grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

#직사각형 칠하기(1로 표시)
for i in range(2): 
    for x in range(x1[i] + OFFSET, x2[i] + OFFSET):
        for y in range(y1[i] + OFFSET, y2[i] + OFFSET):
            grid[x][y] = 1

# 직사각형영역 지우기(숫자 0으로 덮어쓰기)
# M이 덮은 부분은 0으로 만듬
for x in range(x1[2] + OFFSET, x2[2] + OFFSET):
    for y in range(y1[2] + OFFSET, y2[2] + OFFSET):
        grid[x][y] = 0

#남은 영역개수 세기
area = 0
for i in range(MAX_R + 1):
    area += sum(grid[i])  

print(area)