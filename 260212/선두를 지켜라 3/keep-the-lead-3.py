N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

pos_a = [0]
now = 0
for i in range(N):
    for _ in range(t[i]):
        now += v[i]
        pos_a.append(now)

pos_b = [0]
now = 0
for i in range(M):
    for _ in range(t2[i]):
        now += v2[i]
        pos_b.append(now)

cnt = 0
prev = 3 

for i in range(1, len(pos_a)):
    curr = 3
    if pos_a[i] > pos_b[i]:
        curr = 1
    elif pos_a[i] < pos_b[i]:
        curr = 2
    
    if curr != prev:
        cnt += 1
        prev = curr

print(cnt)