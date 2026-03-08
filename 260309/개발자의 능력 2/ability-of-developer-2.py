ability = list(map(int, input().split()))

# Please write your code here.
import sys

#최솟값을 찾아야 하므로 시스템 최댓값으로 초기화
min_diff = sys.maxsize

total_sum = sum(ability)

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(6):
            for l in range(k + 1, 6):
                
                #첫 번째 팀에서 뽑은 사람과 겹치면 안 됨
                if i == k or i == l or j == k or j == l:
                    continue

                team1_sum = ability[i] + ability[j]
                team2_sum = ability[k] + ability[l]
                
                team3_sum = total_sum - team1_sum - team2_sum
                
                max_team = max(team1_sum, team2_sum, team3_sum)
                min_team = min(team1_sum, team2_sum, team3_sum)
                
                diff = max_team - min_team
                
                min_diff = min(min_diff, diff)

print(min_diff)