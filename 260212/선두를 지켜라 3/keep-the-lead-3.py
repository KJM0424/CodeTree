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
pos_a = []
cur_loc = 0
for i in range(N):
    for _ in range(t[i]):
        cur_loc += v[i]
        pos_a.append(cur_loc)

pos_b = []
cur_loc = 0
for i in range(M):
    for _ in range(t2[i]):
        cur_loc += v2[i]
        pos_b.append(cur_loc)

ans = 0
prev_status = -1  

for i in range(len(pos_a)):
    if pos_a[i] > pos_b[i]:
        curr_status = 1  # A 
    elif pos_a[i] < pos_b[i]:
        curr_status = 2  # B 
    else:
        curr_status = 3
    if i == 0:
        prev_status = curr_status
        continue
    
    if curr_status != prev_status:
        ans += 1
        prev_status = curr_status

print(ans)