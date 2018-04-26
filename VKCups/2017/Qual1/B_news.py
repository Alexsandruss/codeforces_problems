# Conditions - http://codeforces.com/contest/769/problem/B
class Student:
    def __init__(self, number, messages):
        self.number = number
        self.messages = messages
        self.knowledge = False

    def sent_message(self, another_student):
        if self.knowledge is False or self.messages == 0:
            raise ValueError
        self.messages -= 1
        another_student.knowledge = True


count = int(input())
input_array = input()
input_array = input_array.split(" ")

students = []
for i in range(count):
    new_student = Student(i+1, int(input_array[i]))
    students.append(new_student)
students[0].knowledge = True
knowledge_count = 1
current_sender = students[0]
log = ""
knowledge = True
messages_count = 0
while knowledge_count < count:
    for i in range(current_sender.messages):
        max_messages = -1
        current_getter = None
        for student in students:
            if student.knowledge is False and student.messages > max_messages:
                current_getter = student
                max_messages = student.messages
        if current_getter is None:
            break
        else:
            current_sender.sent_message(current_getter)
            messages_count += 1
            log += str(current_sender.number)+" "+str(current_getter.number)+"\n"
            knowledge_count += 1
    max_messages = 0
    for student in students:
        if student.knowledge is True and student.messages > max_messages:
            current_sender = student
            max_messages = student.messages
    if max_messages == 0 and knowledge_count < count:
        knowledge = False
        break

if knowledge is True:
    print(messages_count)
    log = log[:(len(log)-1)]
    print(log)
else:
    print(-1)
"""
All tests passed
Time: 62 ms
Memory: 5496 KB
http://codeforces.com/contest/769/submission/35601961
"""