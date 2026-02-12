n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.

pos_a = [0]
cur = 0
for i in range(n):
    for _ in range(t[i]):
        if d[i] == 'R':
            cur += 1
        else:
            cur -= 1
        pos_a.append(cur)

pos_b = [0]
cur = 0
for i in range(m):
    for _ in range(t_b[i]):
        if d_b[i] == 'R':
            cur += 1
        else:
            cur -= 1
        pos_b.append(cur)

if len(pos_a) < len(pos_b):
    last = pos_a[-1]
    for _ in range(len(pos_b) - len(pos_a)):
        pos_a.append(last)
elif len(pos_b) < len(pos_a):
    last = pos_b[-1]
    for _ in range(len(pos_a) - len(pos_b)):
        pos_b.append(last)

ans = 0
for i in range(1, len(pos_a)):
    if pos_a[i] == pos_b[i]:
        if pos_a[i-1] != pos_b[i-1]:
            ans += 1

print(ans)