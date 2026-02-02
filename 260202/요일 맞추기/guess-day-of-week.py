m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def day_of_year(m, d):
    return sum(days[1:m]) + d

day1 = day_of_year(m1, d1)
day2 = day_of_year(m2, d2)
diff = day2 - day1

first_weekday = input().strip()

start_index = weekdays.index(first_weekday)

result_index = (start_index + diff) % 7
print(weekdays[result_index])