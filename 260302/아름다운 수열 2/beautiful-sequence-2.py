N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
sorted_B = sorted(B)
cnt = 0

for i in range(N - M + 1):
    
    sub_A = A[i : i + M]
    
    if sorted(sub_A) == sorted_B:
        cnt += 1

print(cnt)