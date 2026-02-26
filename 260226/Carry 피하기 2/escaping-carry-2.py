n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def is_carry(a, b, c):
    while a > 0 or b > 0 or c > 0:
        digit_sum = (a % 10) + (b % 10) + (c % 10)
        
        if digit_sum >= 10:
            return True
            
        a //= 10
        b //= 10
        c //= 10
        
    return False 

max_sum = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            
            # 고른 3개의 수에서 Carry가 발생하지 않는다면?
            if not is_carry(arr[i], arr[j], arr[k]):
                #세 수의 합을 구해 최댓값 갱신
                max_sum = max(max_sum, arr[i] + arr[j] + arr[k])

print(max_sum)