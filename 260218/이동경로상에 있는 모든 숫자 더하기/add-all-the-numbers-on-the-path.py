N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
#시계방향 순서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

#시작 위치(정중앙),초기 방향(북쪽 0)
r, c = N // 2, N // 2
dir_num = 0
ans = board[r][c]  #시작 위치의 숫자도 포함해서 덧셈 시작

for cmd in str:
    if cmd == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4
    else: 
        nr, nc = r + dxs[dir_num], c + dys[dir_num]
        
        #격자 범위 내일 때만 이동 및 숫자 더하기
        if 0 <= nr < N and 0 <= nc < N:
            r, c = nr, nc
            ans += board[r][c]

print(ans)