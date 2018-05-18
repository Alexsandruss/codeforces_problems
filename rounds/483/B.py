# Conditions - http://codeforces.com/contest/984/problem/B
n, m = [int(el) for el in input().split()]
field = []
for i in range(n):
    field.append(input())
correct = True
for y in range(n):
    for x in range(m):
        if field[y][x] == "*":
            continue
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if x+dx < 0 or x+dx > m-1 or y+dy < 0 or y+dy > n-1 or (dy == 0 and dx == 0):
                    continue
                if field[y+dy][x+dx] == "*":
                    count += 1
        if field[y][x] == ".":
            input_count = 0
        else:
            input_count = int(field[y][x])
        if input_count != count:
            correct = False
            break
    if not correct:
        break
if correct:
    print("YES")
else:
    print("NO")
# all tests passed - http://codeforces.com/contest/984/submission/38405726
