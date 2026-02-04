a, b = map(int, input().split())
n = input()

# Please write your code here.
num = 0
for digit in n:
    num = num * a + int(digit)

digits = []
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit, end="")