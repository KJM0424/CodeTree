n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0

for i in range(n):

    for j in range(i, n):
        
        sub_arr = arr[i : j + 1]
        
        total_sum = sum(sub_arr)
        length = len(sub_arr)

        if total_sum % length == 0:
            avg = total_sum // length
            
            if avg in sub_arr:
                cnt += 1

print(cnt)