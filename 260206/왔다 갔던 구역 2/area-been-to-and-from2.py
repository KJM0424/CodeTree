n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
offset = 1000
arr = [0] * 2005
cur = offset

for i in range(n):
    dist = x[i]
    direction = dir[i]
    
    if direction == 'R':
        for j in range(cur, cur + dist):
            arr[j] += 1
        cur += dist
    else:
        for j in range(cur - dist, cur):
            arr[j] += 1
        cur -= dist

ans = 0
for val in arr:
    if val >= 2:
        ans += 1

print(ans)