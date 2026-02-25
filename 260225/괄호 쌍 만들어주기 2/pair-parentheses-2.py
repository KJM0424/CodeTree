A = input()

# Please write your code here.
n = len(A)
cnt = 0
for i in range(n - 1):
    if A[i] == '(' and A[i+1] == '(':
    
        # '((' 뒤에 나와야 하므로 i + 2부터 탐색 시작
        for j in range(i + 2, n - 1):
            if A[j] == ')' and A[j+1] == ')':
                cnt += 1

print(cnt)