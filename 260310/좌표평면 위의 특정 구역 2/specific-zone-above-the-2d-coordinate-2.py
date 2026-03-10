n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys

min_area = sys.maxsize

for i in range(n):

    min_x, max_x = sys.maxsize, 0
    min_y, max_y = sys.maxsize, 0
    
    for j in range(n):
        if i == j:
            continue
        min_x = min(min_x, x[j])
        max_x = max(max_x, x[j])
        min_y = min(min_y, y[j])
        max_y = max(max_y, y[j])
        
    area = (max_x - min_x) * (max_y - min_y)
    
    min_area = min(min_area, area)

print(min_area)