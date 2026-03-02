n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
MAX_POS = 10000
arr = [0] * (MAX_POS + 1)

for i in range(n):
    if c[i] == 'G':
        arr[x[i]] = 1
    else:
        arr[x[i]] = 2

max_score = 0

for i in range(MAX_POS - k + 1):
    current_score = 0
    
    for j in range(i, i + k + 1):
        current_score += arr[j]
        

    max_score = max(max_score, current_score)

print(max_score)