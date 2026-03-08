N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def get_dist(x, y):
    straight_dist = abs(x - y)
    circular_dist = N - abs(x - y)
    
    return min(straight_dist, circular_dist)

cnt = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            
            cond1 = (get_dist(i, a1) <= 2 and get_dist(j, b1) <= 2 and get_dist(k, c1) <= 2)

            cond2 = (get_dist(i, a2) <= 2 and get_dist(j, b2) <= 2 and get_dist(k, c2) <= 2)
            
            if cond1 or cond2:
                cnt += 1

print(cnt)