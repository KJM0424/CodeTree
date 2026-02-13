n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
#시작 위치 초기화
x, y = 0, 0

# 동서남북 순서로 설정
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dir_mapper = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3
}

for i in range(n):
    dir_num = dir_mapper[dir[i]]
    
    #이동할 방향 * 거리를 현재 위치에 더하기
    x += dx[dir_num] * dist[i]
    y += dy[dir_num] * dist[i]

print(x, y)