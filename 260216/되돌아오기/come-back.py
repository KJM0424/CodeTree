N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
mapper = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

x, y = 0, 0
time = 0
ans = -1

for i in range(N):
    dir_num = mapper[dir[i]]
    
    for _ in range(dist[i]):
        x += dxs[dir_num]
        y += dys[dir_num]
        time += 1
        
        if x == 0 and y == 0:
            ans = time
            break
            
    if ans != -1:
        break

print(ans)