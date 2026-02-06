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
arr = [0] * 200001

for i in range(n):
    dist = x[i]
    d = dir[i]
    
    if d == 'L':
        for j in range(cur, cur - dist, -1):
            arr[j] = 1
        cur -= (dist - 1)
    else:
        for j in range(cur, cur + dist):
            arr[j] = 2
        cur += (dist - 1)

white = arr.count(1)
black = arr.count(2)
print(white, black)