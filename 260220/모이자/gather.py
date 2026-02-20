n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys

min_dist = sys.maxsize

for i in range(n):
    sum_dist = 0
    
    for j in range(n):
        sum_dist += A[j] * abs(i - j)
        
    if sum_dist < min_dist:
        min_dist = sum_dist

print(min_dist)