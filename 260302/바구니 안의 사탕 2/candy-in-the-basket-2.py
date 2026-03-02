N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
MAX_POS = 100
arr = [0] * (MAX_POS + 1)

for c, p in zip(candy, pos):
    arr[p] += c

max_candies = 0
window_size = 2 * K + 1


for i in range(MAX_POS + 1):
    
    current_candies = sum(arr[i : i + window_size])
    
    max_candies = max(max_candies, current_candies)

print(max_candies)