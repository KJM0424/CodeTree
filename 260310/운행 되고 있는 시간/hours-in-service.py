n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
max_time = 0

for i in range(n):
    working = [0] * 1001
    
    for j in range(n):
        if i == j:
            continue
            
        for k in range(a[j], b[j]):
            working[k] = 1
            
    max_time = max(max_time, sum(working))

print(max_time)