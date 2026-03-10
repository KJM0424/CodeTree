n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0

for i in range(n):
    overlap = False
    
    for j in range(n):
        if i == j:
            continue
            
        x1_i, x2_i = lines[i]
        x1_j, x2_j = lines[j]
        
        if (x1_i < x1_j and x2_i > x2_j) or (x1_i > x1_j and x2_i < x2_j):
            overlap = True
            break
            
    if not overlap:
        ans += 1

print(ans)