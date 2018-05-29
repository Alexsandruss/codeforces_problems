# Conditions - https://codeforces.com/contest/981/problem/A
word = input()
if word != word[::-1]:
    print(len(word))
else:
    max_len = 0
    for i in range(1, len(word)):
        if word[i:] != word[i:][::-1] and len(word)-i > max_len:
            max_len = len(word)-i
        if word[:len(word)-i] != word[:len(word)-i][::-1] and len(word)-i > max_len:
            max_len = len(word)-i
    print(max_len)
# all tests passed (109 ms/16 KB) - https://codeforces.com/contest/981/submission/38659724
