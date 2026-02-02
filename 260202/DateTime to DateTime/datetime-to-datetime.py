a, b, c = map(int, input().split())

# Please write your code here.

start = 10 * 1440 + 11 * 60 + 11
end = (a - 1) * 1440 + b * 60 + c

print(end - start if end >= start else -1)