n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys

#최솟값을 구해야 하므로 시스템 최댓값으로 초기화
min_dist = sys.maxsize

#건너뛸 체크포인트고정 
for i in range(1, n - 1):
    dist = 0
    prev_idx = 0 
    
    # 나머지 체크포인트들을 순서대로 방문하며 거리 계산
    for j in range(1, n):
        if j == i:  # 건너뛰기 무시
            continue
            
        dist += abs(x[prev_idx] - x[j]) + abs(y[prev_idx] - y[j])
        prev_idx = j 
        
    min_dist = min(min_dist, dist)

print(min_dist)