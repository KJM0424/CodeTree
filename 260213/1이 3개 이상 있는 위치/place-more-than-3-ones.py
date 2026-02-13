n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    #격자 안에 들어오는지 확인
    return 0 <= x and x < n and 0 <= y and y < n

# 좌우상하 순서
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

ans = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        
        #현재 칸(i, j)을 기준으로 4방향 탐색
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            
            # in_range(nx, ny)를 먼저 확인
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        
        #인접한 1의 개수가 3개 이상이면 정답 횟수 증가
        if cnt >= 3:
            ans += 1

print(ans)