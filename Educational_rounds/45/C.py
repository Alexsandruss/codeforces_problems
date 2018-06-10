n = int(input())
substrings = []
for i in range(n):
    substrings.append(input())
comb_count = 0
s_dict = {}
for si in substrings:
    if si not in s_dict.keys():
        count = 0
        for symbol in si:
            if symbol == "(":
                count += 1
            else:
                count -= 1
        s_dict.update({si: count})
for si in substrings:
    for sj in substrings:
        if s_dict[si] + s_dict[sj] != 0:
            print("breaked")
            continue
        sij = si+sj
        count = 0
        for symbol in sij:
            if symbol == "(":
                count += 1
            else:
                count -= 1
            if count < 0:
                break
        if count == 0:
            comb_count += 1
print(comb_count)
