m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def count_days(m, d):
    total_days = 0
    for i in range(1, m):
        total_days += days_of_month[i]
    total_days += d

    return total_days

diff = count_days(m2, d2) - count_days(m1, d1)
print(week_days[diff % 7])