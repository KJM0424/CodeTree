n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

import sys

min_dist = sys.maxsize

for i in range(n):
    dist = 0
    
    for j in range(n):
        #시계 반대 방향(오른쪽)으로 이동할 때의 거리 계산
        move_cnt = (j - i + n) % n
        
        #방으로 가야 하는 인원수 * 이동 거리
        dist += a[j] * move_cnt
        
    min_dist = min(min_dist, dist)

print(min_dist)