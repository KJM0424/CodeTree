a = input()

# Please write your code here.
a_list = list(a)
max_val = 0

for i in range(len(a_list)):
    a_list[i] = '1' if a_list[i] == '0' else '0'
    
    curr_val = int("".join(a_list), 2)
    max_val = max(max_val, curr_val)
    
    a_list[i] = '1' if a_list[i] == '0' else '0'

print(max_val)