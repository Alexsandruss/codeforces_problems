# Conditions - http://codeforces.com/contest/877/problem/A
line = input()
names_count = {"Danil": 0, "Olya": 0, "Slava": 0, "Ann": 0, "Nikita": 0}
for name in names_count.keys():
    while name in line:
        names_count[name] += 1
        line = line.replace(name, "#", 1)
count = 0
for name in names_count.keys():
    count += names_count[name]
if count == 1:
    print("YES")
else:
    print("NO")
# all tests passed - http://codeforces.com/contest/877/submission/38544816
