N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dxs = [-1, 1, 0, 0, -1, -1, 1, 1]
dys = [0, 0, -1, 1, -1, 1, -1, 1]

cnt = 0

for i in range(N):
    for j in range(M):
        
        #'L'일 때만 탐색 시작
        if arr[i][j] == 'L':
            
            #8방향으로 각각 뻗어나가 보기
            for dx, dy in zip(dxs, dys):
                match = True
                
                for step in range(1, 3):
                    nx = i + dx * step
                    ny = j + dy * step
                    
                    #격자를 벗어나거나, 칸의 문자가 'E'가 아니면 실패
                    if not (0 <= nx < N and 0 <= ny < M) or arr[nx][ny] != 'E':
                        match = False
                        break

                if match:
                    cnt += 1

print(cnt)