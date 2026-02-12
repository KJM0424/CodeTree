N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
ans = -1  
penalty_counts = [0] * (N + 1)

for s in student:
    penalty_counts[s] += 1
    
    if penalty_counts[s] >= K:
        ans = s
        break  

print(ans)