n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

offset = 100
arr = [0] * 205

for x1, x2 in segments:
    x1 += offset
    x2 += offset
    
    for i in range(x1, x2):
        arr[i] += 1

print(max(arr))