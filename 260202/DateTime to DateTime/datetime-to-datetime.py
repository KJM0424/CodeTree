a, b, c = map(int, input().split())

# Please write your code here.
start_day = 11
start_hour = 11
start_min = 11
start_total = (start_day - 1) * 24 * 60 + start_hour * 60 + start_min

end_total = (a - 1) * 24 * 60 + b * 60 + c

result = end_total - start_total
print(result) 