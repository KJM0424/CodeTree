n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
pos_a = []
cur_loc = 0
for i in range(n):
    for _ in range(t[i]):
        cur_loc += v[i] 
        pos_a.append(cur_loc)

pos_b = []
cur_loc = 0
for i in range(m):
    for _ in range(t2[i]):
        cur_loc += v2[i]
        pos_b.append(cur_loc)

leader = 0  
ans = 0

for i in range(len(pos_a)):
    if pos_a[i] > pos_b[i]: 
        if leader == 2:
            ans += 1
        leader = 1 

    elif pos_a[i] < pos_b[i]: 
        if leader == 1:
            ans += 1
        leader = 2


print(ans)