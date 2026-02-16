commands = input()

# Please write your code here.
#시계방향 세팅
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 초기 상태
x, y = 0, 0
dir_num = 0
time = 0
ans = -1

for cmd in commands:
    if cmd == 'L':
        # 왼쪽으로
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd == 'R':
        # 오른쪽으로회전
        dir_num = (dir_num + 1) % 4
    else: # cmd == 'F'
        # 바라보는 방향으로 1칸 전진
        x += dxs[dir_num]
        y += dys[dir_num]
        
    # 이동이든 회전이든 무조건 1초가 소모됨
    time += 1
    
    #동작 직후 원점(0, 0)에 돌아왔는지 확인
    if x == 0 and y == 0:
        ans = time
        break

print(ans)