# Conditions - https://codeforces.com/contest/987/problem/A
n = int(input())
color_to_stone = {
    "purple": "Power",
    "green": "Time",
    "blue": "Space",
    "orange": "Soul",
    "red": "Reality",
    "yellow": "Mind"
}
colors = []
for i in range(n):
    colors.append(input())
print(6-n)
for color in colors:
    color_to_stone.pop(color)
for c in color_to_stone.keys():
    print(color_to_stone[c])
# all tests passed - https://codeforces.com/contest/987/submission/38764156
