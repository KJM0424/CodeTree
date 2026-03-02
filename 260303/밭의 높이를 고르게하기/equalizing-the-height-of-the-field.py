N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys

min_cost = sys.maxsize

for i in range(N - T + 1):
    current_cost = 0
    
    for j in range(i, i + T):
        
        current_cost += abs(arr[j] - H)
        
    min_cost = min(min_cost, current_cost)

print(min_cost)