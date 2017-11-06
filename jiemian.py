#coding=utf-8


import Tkinter
#import basicwork as bk
import tkMessageBox
import pickle
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt




with open('student.pkl', 'rb') as input1:
    student_dict = pickle.load(input1)

with open('teacher.pkl', 'rb') as input2:
    teacher_dict = pickle.load(input2)

with open('administrator.pkl', 'rb') as input3:
    administrator_dict = pickle.load(input3)

def reverse_sort():
    tkMessageBox.showinfo(message= sorted(student_dict.items(), key=lambda d: d[1],reverse=True))

def Sort():
    tkMessageBox.showinfo(message=sorted(student_dict.items(), key=lambda d: d[1]))


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



def scores_analyze():
    l = []
    for i in student_dict:
        l.append(student_dict[i])
    scores = np.array(l)
    tkMessageBox.showinfo(message='mean = %d,max = %d,min = %d'%(scores.mean(),scores.max(),scores.min()))


def main():
    root = Tkinter.Tk()

    def show_student():
        student_menu_1()

    def show_teacher():
        teacher_menu_1()

    def show_administrator():
        admini_menu_1()

    buttonstudent = Tkinter.Button(root,text = 'student',command = show_student)
    buttonstudent.place(x=50,y=20,width=110,height=20)
    buttonteacher = Tkinter.Button(root,text = 'teacher',command = show_teacher)
    buttonteacher.place(x=50,y=50,width=110,height=20)
    buttontadministrator = Tkinter.Button(root,text = 'administrator',command = show_administrator)
    buttontadministrator.place(x=50,y=80,width=110,height=20)
    root.mainloop()

def student_menu_1():
    root = Tkinter.Tk()
    labelName = Tkinter.Label(root,text = '学生',justify = Tkinter.RIGHT, width = 80)
    labelName.place(x=20,y=35,width = 80,height =20)
    student_name = Tkinter.StringVar(root,value='')
    entryName = Tkinter.Entry(root,width = 80, textvariable = student_name)
    entryName.place(x=100,y=35,width=80,height=20)

    def ensure():

        if student_name.get() in student_dict.keys():
            student_menu_2()
        else:
            tkMessageBox.showinfo(message="没有此学生")

    buttonsure = Tkinter.Button(root,text = '确定',command = ensure)
    buttonsure.place(x=90,y=80,width=50,height=20)
    root.mainloop()

def student_menu_2():
    root = Tkinter.Tk()

    def analyze():
        scores_analyze()

    button1 = Tkinter.Button(root,text = '分析',command = analyze)
    button1.place(x=50,y=50,width=50,height=20)

    def graph1():
        graph()
    button2 = Tkinter.Button(root,text = '图标',command = graph1)
    button2.place(x=110,y=50,width=50,height=20)

    def sort():
        Sort()
    buutton3 = Tkinter.Button(root,text = '排序',command = sort)
    buutton3.place(x=50,y=80,width=50,height=20)

    def reverse():
        reverse_sort()
    button4 = Tkinter.Button(root,text = '倒排',command = reverse)
    button4.place(x=110,y=80,width = 50,height=20)
    root.mainloop()

def teacher_menu_1():
    root = Tkinter.Tk()
    labelName = Tkinter.Label(root, text='老师', justify=Tkinter.RIGHT, width=80)
    labelName.place(x=20, y=35, width=80, height=20)
    teacher_name = Tkinter.StringVar(root, value='')
    entryName = Tkinter.Entry(root, width=80, textvariable=teacher_name)
    entryName.place(x=100, y=35, width=80, height=20)

    labelPassword = Tkinter.Label(root, text='密码', justify=Tkinter.RIGHT, width=80)
    labelPassword.place(x=20, y=70, width=80, height=20)
    teacher_password = Tkinter.StringVar(root, value='')
    entryPassword = Tkinter.Entry(root, width=80, textvariable=teacher_password)
    entryPassword.place(x=100, y=70, width=80, height=20)

    def sure():
        if teacher_name.get() in teacher_dict.keys():
            global TEACHER
            TEACHER = teacher_name.get()
            if teacher_dict[teacher_name.get()] == teacher_password.get():
                teacher_menu_2()
            else:
                tkMessageBox.showinfo(message='密码错误')
        else:
            tkMessageBox.showinfo(message='没有此老师')

    button1 = Tkinter.Button(root,text='确认',command = sure)
    button1.place(x=70,y=110,width=80,height = 20)
    root.mainloop()

def teacher_menu_2():
    root = Tkinter.Tk()
    delete_student_name = Tkinter.StringVar(root,value='')
    entryName1 = Tkinter.Entry(root,width=80,textvariable = delete_student_name)
    entryName1.place(x=20,y=35,width=80,height=20)
    student_name = Tkinter.StringVar(root,value='')
    entryName2 = Tkinter.Entry(root,width=80,textvariable=student_name)
    entryName2.place(x=20,y=80,width=80,height=20)
    student_score = Tkinter.StringVar(root,value='')
    entryScore = Tkinter.Entry(root,width=80,textvariable = student_score)
    entryScore.place(x=20,y=105,width = 80,height=20)
    def delete():
        if delete_student_name.get() in student_dict.keys():
            del student_dict[delete_student_name.get()]
            with open('student.pkl', 'wb') as output1:
                pickle.dump(student_dict, output1)
            tkMessageBox.showinfo(message='此学生已经删除')
        else:
            tkMessageBox.showinfo(message='无此学生')
    button1 = Tkinter.Button(root,text='删除',command = delete)
    button1.place(x=110,y=35,width=80,height = 20)

    def add():
        student_dict[student_name.get()]= int (student_score.get())
        with open('student.pkl', 'wb') as output1:
            pickle.dump(student_dict, output1)
        tkMessageBox.showinfo(message='此学生已经添加')

    button2 = Tkinter.Button(root,text='添加',command = add)
    button2.place(x=110,y=80,width = 80,height = 20)

    def change():
        if student_name.get() in student_dict.keys():
            student_dict[student_name.get()] = int(student_score.get())
            with open('student.pkl', 'wb') as output1:
                pickle.dump(student_dict, output1)
            tkMessageBox.showinfo(message='成绩更新完成')
        else:
            tkMessageBox.showinfo(message='无此学生')
    button3 = Tkinter.Button(root,text='更改',command = change)
    button3.place(x=110,y=105,width = 80,height = 20)

    def change_password():
        teacher_menu_3()
    button4 = Tkinter.Button(root,text='更改密码',command = change_password)
    button4.place(x=50,y=150,width = 100,height = 20)
    root.mainloop()

def teacher_menu_3():
    root = Tkinter.Tk()
    label = Tkinter.Label(root,text='新密码',width = 80)
    label.place(x=60,y=20,width =80,height = 20)
    teacher_password = Tkinter.StringVar(root,value='')
    entrypassword = Tkinter.Entry(root,width = 100,textvariable = teacher_password)
    entrypassword.place(x=50,y=50,width = 100,height = 20)

    def sure():
        teacher_dict[TEACHER] = teacher_password.get()
        with open('teacher.pkl', 'wb') as output2:
            pickle.dump(teacher_dict, output2)
        tkMessageBox.showinfo(message='密码设置完成')
    button = Tkinter.Button(root,text='确定',command = sure)
    button.place(x=75,y=100,width = 50,height = 20)
    root.mainloop()

def admini_menu_1():
    root = Tkinter.Tk()
    labelName = Tkinter.Label(root, text='管理员', justify=Tkinter.RIGHT, width=80)
    labelName.place(x=20, y=35, width=80, height=20)
    admini_name = Tkinter.StringVar(root, value='')
    entryName = Tkinter.Entry(root, width=80, textvariable=admini_name)
    entryName.place(x=100, y=35, width=80, height=20)

    labelPassword = Tkinter.Label(root, text='密码', justify=Tkinter.RIGHT, width=80)
    labelPassword.place(x=20, y=70, width=80, height=20)
    admini_password = Tkinter.StringVar(root, value='')
    entryPassword = Tkinter.Entry(root, width=80, textvariable=admini_password)
    entryPassword.place(x=100, y=70, width=80, height=20)

    def sure():
        if admini_name.get() in administrator_dict.keys():
            global ADMINI
            ADMINI= admini_name.get()
            if administrator_dict[admini_name.get()] == admini_password.get():
                admini_menu_2()
            else:
                tkMessageBox.showinfo(message='密码错误')
        else:
            tkMessageBox.showinfo(message='没有此管理员')


    button1 = Tkinter.Button(root, text='确认', command=sure)
    button1.place(x=70, y=110, width=80, height=20)
    root.mainloop()

def admini_menu_3():
    root = Tkinter.Tk()
    label = Tkinter.Label(root, text='新密码', width=80)
    label.place(x=60, y=20, width=80, height=20)
    admini_password = Tkinter.StringVar(root, value='')
    entrypassword = Tkinter.Entry(root, width=100, textvariable=admini_password)
    entrypassword.place(x=50, y=50, width=100, height=20)

    def sure():
        administrator_dict[ADMINI] = admini_password.get()
        with open('administrator.pkl', 'wb') as output3:
            pickle.dump(administrator_dict, output3)
        tkMessageBox.showinfo(message='密码设置完成')
    button = Tkinter.Button(root, text='确定', command=sure)
    button.place(x=75, y=100, width=50, height=20)
    root.mainloop()

def admini_menu_2():
    root = Tkinter.Tk()
    delete_name = Tkinter.StringVar(root, value='')
    entryName1 = Tkinter.Entry(root, width=80, textvariable=delete_name)
    entryName1.place(x=20, y=35, width=80, height=20)
    name = Tkinter.StringVar(root, value='')
    entryName2 = Tkinter.Entry(root, width=80, textvariable=name)
    entryName2.place(x=20, y=80, width=80, height=20)
    score_or_password = Tkinter.StringVar(root, value='')
    entryScore = Tkinter.Entry(root, width=80, textvariable=score_or_password)
    entryScore.place(x=20, y=105, width=80, height=20)

    def delete():
        pass

    button1 = Tkinter.Button(root, text='删除', command=delete)
    button1.place(x=110, y=35, width=80, height=20)

    def add():
        pass

    button2 = Tkinter.Button(root, text='添加', command=add)
    button2.place(x=110, y=80, width=80, height=20)

    def change():
        pass

    button3 = Tkinter.Button(root, text='更改', command=change)
    button3.place(x=110, y=105, width=80, height=20)

    def change_password():
        admini_menu_3()

    button4 = Tkinter.Button(root, text='更改密码', command=change_password)
    button4.place(x=50, y=150, width=100, height=20)
    root.mainloop()


main()




