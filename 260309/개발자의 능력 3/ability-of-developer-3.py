abilities = list(map(int, input().split()))

# Please write your code here.
import sys

total_sum = sum(abilities)

min_diff = sys.maxsize

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            
            team1_sum = abilities[i] + abilities[j] + abilities[k]
            
            team2_sum = total_sum - team1_sum
            
            diff = abs(team1_sum - team2_sum)
            min_diff = min(min_diff, diff)

print(min_diff)