n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_sum = 0

for i in range(n):
    
    for j in range(i + 2, n):
        
        #두 수의 합을 구하고 최댓값 갱신
        curr_sum = numbers[i] + numbers[j]
        max_sum = max(max_sum, curr_sum)

print(max_sum)
