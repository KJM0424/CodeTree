n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

#반대 방향끼리 합이 3이 되도록 매핑 (U-D, R-L)
dxs = [-1, 0, 0, 1]
dys = [0, 1, -1, 0]

mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

x, y = r - 1, c - 1
dir_num = mapper[d]

#격자 범위 확인 함수
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    #다음 위치가 격자 안이라면 정상 이동
    if in_range(nx, ny):
        x, y = nx, ny
        
    else:
        dir_num = 3 - dir_num

print(x + 1, y + 1)