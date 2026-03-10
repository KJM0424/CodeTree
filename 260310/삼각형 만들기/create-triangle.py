n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
max_area = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k:
                continue
            
            if y[i] == y[j] and x[i] == x[k]:
                area = abs(x[i] - x[j]) * abs(y[i] - y[k])
                max_area = max(max_area, area)

print(max_area)