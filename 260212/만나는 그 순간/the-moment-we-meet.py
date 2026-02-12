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

# Please write your code here.
pos_a = [0] # 0초 위치
current = 0

for i in range(n):
    # 방향에 따라 1초당 이동할 거리 설정
    step = 1 if d[i] == 'R' else -1
    
    # 시간(t[i])만큼 반복하며 매 초마다 위치 기록
    for _ in range(t[i]):
        current += step
        pos_a.append(current)

# --- B의 이동 경로 기록 ---
pos_b = [0]
current = 0

for i in range(m):
    step = 1 if d2[i] == 'R' else -1
    
    for _ in range(t2[i]):
        current += step
        pos_b.append(current)

# --- 최초로 만나는 시간 찾기 ---
ans = -1
# 0초는 제외하고 1초부터 비교
for i in range(1, len(pos_a)):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)