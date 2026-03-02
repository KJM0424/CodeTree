n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_sum = 0

for i in range(n - k + 1):
    interval_sum = 0

    for j in range(i, i + k):
        interval_sum += arr[j]

    max_sum = max(max_sum, interval_sum)

print(max_sum)