# Conditions - http://codeforces.com/contest/522/problem/A
class Repost:
    def __init__(self, name1, name2, reposts):
        self.reposted = name2.lower()
        self.reposter = name1.lower()
        self.depth = 1
        for repost in reposts:
            if repost.reposter == self.reposted:
                self.depth = repost.depth + 1
                break


count = int(input())

notes = []
for i in range(count):
    notes.append(input())

reposts = []
for note in notes:
    names = note.split(" ")
    new_repost = Repost(names[0], names[2], reposts)
    reposts.append(new_repost)

max_depth = 0
for repost in reposts:
    if repost.depth > max_depth:
        max_depth = repost.depth

print(max_depth+1)
"""
All tests passed
Time: 62 ms
Memory: 5528 KB
http://codeforces.com/contest/522/submission/35594816
"""