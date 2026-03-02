n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
arr = sorted(zip(pos, alpha))

max_size = 0

for i in range(n):
    
    for j in range(i, n):
        
        sub_alphas = [c for p, c in arr[i : j + 1]]
        
        g_cnt = sub_alphas.count('G')
        h_cnt = sub_alphas.count('H')
        
        if g_cnt == 0 or h_cnt == 0 or g_cnt == h_cnt:

            size = arr[j][0] - arr[i][0]
            max_size = max(max_size, size)

print(max_size)