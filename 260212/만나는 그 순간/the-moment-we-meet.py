n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

pos_a = [0]
current = 0

for i in range(n):

    step = 1 if d[i] == 'R' else -1
    
    for _ in range(t[i]):
        current += step
        pos_a.append(current)

pos_b = [0]
current = 0

for i in range(m):
    step = 1 if d2[i] == 'R' else -1
    
    for _ in range(t2[i]):
        current += step
        pos_b.append(current)

ans = -1
for i in range(1, len(pos_a)):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)