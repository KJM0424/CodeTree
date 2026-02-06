n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
offset = 100000
cur = offset
color = [0] * 200001
cnt_w = [0] * 200001
cnt_b = [0] * 200001

for i in range(n):
    dist = x[i]
    d = dir[i]

    if d == 'L':
        for k in range(cur, cur - dist, -1):
            cnt_w[k] += 1
            if cnt_w[k] >= 2 and cnt_b[k] >= 2:
                color[k] = 3
            elif color[k] != 3:
                color[k] = 1
        cur -= (dist - 1)
        
    else:
        for k in range(cur, cur + dist):
            cnt_b[k] += 1
            if cnt_w[k] >= 2 and cnt_b[k] >= 2:
                color[k] = 3
            elif color[k] != 3:
                color[k] = 2
        cur += (dist - 1)

w, b, g = 0, 0, 0
for i in range(200001):
    if color[i] == 1: w += 1
    elif color[i] == 2: b += 1
    elif color[i] == 3: g += 1

print(w, b, g)