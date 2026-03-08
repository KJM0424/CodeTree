arr = list(map(int, input().split()))

# Please write your code here.
import sys

min_diff = sys.maxsize

is_possible = False

total_sum = sum(arr)

for i in range(5):
    for j in range(i + 1, 5):
        
        for k in range(5):
            for l in range(k + 1, 5):

                if i == k or i == l or j == k or j == l:
                    continue
                    
                team1 = arr[i] + arr[j]
                team2 = arr[k] + arr[l]
                
                team3 = total_sum - team1 - team2
                
                if team1 != team2 and team2 != team3 and team1 != team3:
                    is_possible = True
                    
                    max_team = max(team1, team2, team3)
                    min_team = min(team1, team2, team3)
                    
                    diff = max_team - min_team
                    min_diff = min(min_diff, diff)

if not is_possible:
    print(-1)
else:
    print(min_diff)