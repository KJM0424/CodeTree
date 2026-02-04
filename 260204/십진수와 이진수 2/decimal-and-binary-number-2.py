N = input()

# Please write your code here.
num = 0
for digit in N:
    num = num * 2 + int(digit)
num = num * 17

digits = []
while True:
    if num < 2:
        digits.append(num)
        break
    
    digits.append(num % 2)
    num //= 2

for digit in digits[::-1]:
    print(digit, end="")