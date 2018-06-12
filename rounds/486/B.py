n = int(input())
strings = {}
for i in range(n):
    new_s = input()
    if new_s not in strings.keys():
        strings.update({new_s: [1, 0]})
    else:
        strings[new_s][0] += 1
for s1 in strings.keys():
    for s2 in strings.keys():
        if s1 == s2:
            continue
        if s1 in s2:
            strings[s1][1] += 1
if list(range(0, len(strings))) != sorted([strings[s][1] for s in strings.keys()]):
    print("NO")
else:
    print("YES")
    while len(strings) != 0:
        mx = -1
        mx_s = ""
        for s in strings.keys():
            if strings[s][1] > mx:
                mx = strings[s][1]
                mx_s = s
        for i in range(strings[mx_s][0]):
            print(mx_s)
        strings.__delitem__(mx_s)
