# coding=utf-8

import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('student.pkl', 'rb') as input1:
    student_dict = pickle.load(input1)

with open('teacher.pkl', 'rb') as input2:
    teacher_dict = pickle.load(input2)

with open('administrator.pkl', 'rb') as input3:
    administrator_dict = pickle.load(input3)


# read from files

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def search_score(self):
        print(student_dict[self.name])


class Teacher(object):
    def __init__(self, name, teacher_password):
        self.name = name
        self.teacher_password = teacher_password
        teacher_dict[self.name] = teacher_password

    def adds_student(self, student):
        student_dict[student.name] = student.score

    def suspend_student(self, student):
        del student_dict[student.name]

    def revise_scores(self, student, new_score):
        student_dict[student.name] = new_score

    def revise_teacher_password(self, new_password):
        teacher_dict[self.name] = new_password


class Administrator(object):
    def __init__(self, name, administrator_password):
        self.name = name
        self.administrator_password = administrator_password
        administrator_dict[self.name] = administrator_password

    def adds_student(self, student):
        student_dict[student.name] = student.score

    def suspend_student(self, student):
        del student_dict[student.name]

    def revise_scores(self, student, new_score):
        student_dict[student.name] = new_score

    def adds_teacher(self, teacher):
        teacher_dict[teacher.name] = teacher.phone_num

    def suspend_teacher(self, teacher):
        del student_dict[teacher.name]

    def adds_administrator(self, administrator):
        administrator_dict[administrator.name] = administrator.phone_num

    def suspend_administrator(self, administrator):
        del administrator_dict[administrator.name]

    def revise_administrator_password(self, new_password):
        administrator_dict[self.name] = new_password


def graph():
    names = []
    y = []
    for i in student_dict:
        names.append(i)
        y.append(student_dict[i])

    x = range(len(names))
    plt.plot(x, y, 'ro-')
    plt.xticks(x, names, rotation=45)
    plt.margins(0.08)
    plt.subplots_adjust(bottom=0.15)
    plt.show()


def sort():
    print(sorted(student_dict.items(), key=lambda d: d[1]))


def reverse_sort():
    print(sorted(student_dict.items(), key=lambda d: d[1], reverse=True))


def scores_analyze():
    l = []
    for i in student_dict:
        l.append(student_dict[i])
    scores = np.array(l)
    print('mean = %d,max = %d,min = %d' % (scores.mean(), scores.max(), scores.min()))


def identify_student(student_name):
    if student_name in student_dict.keys() == False:
        print('There is not the student')
        # else: enter student interface


def identify_teacher(teacher_name, teacher_password):
    if teacher_name in teacher_dict.keys() == False:
        print('There is not the teacher')
    elif teacher_dict[teacher_name] != teacher_password:
        print('Wrong password')
        # else: enter teacher interface


def identify_administrator(administrator_name, administrator_password):
    if administrator_name in administrator_dict.keys() == False:
        print('There is not the administrator')
    elif administrator_dict[administrator_name] != administrator_password:
        print('Wrong password')
        # else: enter administrator interface


def identify_student_name(student_name):
    if student_name in student_dict.keys() == True:
        print('The student exists')
    elif student_name == '':
        print('null name')
        # else: accept


def identify_teacher_name(teacher_name):
    if teacher_name in teacher_dict.keys() == True:
        print('The teacher exists')
    elif teacher_name == '':
        print('null name')
        # else: accept


def identify_administrator_name(administrator_name):
    if administrator_name in administrator_dict.keys() == True:
        print('The administrator exists')
    elif administrator_name == '':
        print('null name')
        # else: accept


bart = Student('bart simpson', 60)
lisa = Student('lisa simpson', 100)
ralph = Student('ralph wiggum', 0)
sherry = Student('sherry twins', 70)
terry = Student('terry twins', 70)
milhouse = Student('milhouse stupid', 80)
hoover = Teacher('hoover', '30-34-56')
skinner = Administrator('skinner', '30-50-65')

hoover.adds_student(bart)
hoover.adds_student(lisa)
hoover.adds_student(ralph)
hoover.adds_student(sherry)
hoover.adds_student(terry)
hoover.adds_student(milhouse)

# write into files
with open('student.pkl', 'wb') as output1:
    pickle.dump(student_dict, output1)
with open('teacher.pkl', 'wb') as output2:
    pickle.dump(teacher_dict, output2)
with open('administrator.pkl', 'wb') as output3:
    pickle.dump(administrator_dict, output3)
