# Conditions - http://codeforces.com/contest/978/problem/B
n = int(input())
file_name = input()
x_length = 0
count = 0
for symbol in file_name:
    if symbol == "x":
        x_length += 1
    else:
        if x_length - 2 > 0:
            count += x_length - 2
        x_length = 0
if x_length - 2 > 0:
    count += x_length - 2
print(count)
# All tests passed (78 ms/7180 KB) - http://codeforces.com/contest/978/submission/38163453
