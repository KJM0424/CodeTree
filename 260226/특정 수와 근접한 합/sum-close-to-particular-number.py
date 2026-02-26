N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
total_sum = sum(arr)

min_diff = sys.maxsize

for i in range(N):
    for j in range(i + 1, N):
        
        current_sum = total_sum - arr[i] - arr[j]

        diff = abs(S - current_sum)
        min_diff = min(min_diff, diff)

print(min_diff)