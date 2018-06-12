field = input()
cond = False
for i in range(1, len(field)-1):
    s = {field[i-1], field[i], field[i+1]}
    if "." in s:
        continue
    if len(s) == 3:
        cond = True
        break
if cond:
    print("Yes")
else:
    print("No")
