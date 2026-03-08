n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
ans = 0

#1부터 9까지의 숫자로 이루어진 모든 세 자리수 조합 탐색
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            
            #정답이라고 가정한 숫자 조합
            candidate = [i, j, k]
            is_possible = True
            
            #B가 물어본 N개의 질문(조건)을 모두 만족하는지 검사
            for q in range(n):
                q_num = a[q]
                guess = [q_num // 100, (q_num // 10) % 10, q_num % 10]
                
                strike = 0
                ball = 0
                
                for idx in range(3):
                    if candidate[idx] == guess[idx]:
                        strike += 1
                    elif candidate[idx] in guess:
                        ball += 1

                if strike != b[q] or ball != c[q]:
                    is_possible = False
                    break
            
            if is_possible:
                ans += 1

print(ans)