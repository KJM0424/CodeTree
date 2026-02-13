dirs = input()

# Please write your code here.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
dir_num = 0

for cmd in dirs:
    if cmd == 'L':
        #왼쪽(반시계)으로 90도 회전
        #음수가 되는 것을 방지하기 위해 + 4를 해줌
        dir_num = (dir_num - 1 + 4) % 4 
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4
    else: 
        #현재 바라보는 방향으로 1칸 이동
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)