board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
# 탐색 방향 설정(우, 하, 우하대각선, 우상대각선)
dxs = [0, 1, 1, -1]
dys = [1, 0, 1, 1]

def solve():
    for i in range(19):
        for j in range(19):
            #바둑알이 없는칸 패스
            if board[i][j] == 0:
                continue
            
            color = board[i][j]
            
            #현재 바둑알을 기준으로 4가지 방향 찔러보기
            for dx, dy in zip(dxs, dys):
                count = 1  #돌 1개부터 시작
                
                #4칸 더 전진해보기
                for step in range(1, 5):
                    nx, ny = i + dx * step, j + dy * step
                    
                    #격자를 벗어나거나, 돌의 색깔이 다르면 연속이 끊긴 것
                    if not (0 <= nx < 19 and 0 <= ny < 19):
                        break
                    if board[nx][ny] != color:
                        break
                    
                    count += 1
                
                # 승리
                if count == 5:
                    print(color)
                    
                    #문제 조건: 5개 중 가운데돌의 위치를 출력해야 함
                    mid_x = i + dx * 2 + 1
                    mid_y = j + dy * 2 + 1
                    print(mid_x, mid_y)
                    return

    print(0)

solve()