import sys
from student import *
import pickle
FILE_PATH='student_info'


class Mypickle:#自定义pickle模块
    def __init__(self):
        self.path = FILE_PATH
    def dump(self,obj):
        with open(self.path,'ab') as f:
            pickle.dump(obj,f)
    def load(self):
        with open(self.path,'rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except:
                    break
    def del_dump(self,obj):
        with open(self.path,'wb') as f:
            pickle.dump(obj,f)

class StudentManager(object):
    opt_lst = [('添加学员','add_student'), ('删除学员','delete_student'), ('修改学员','mod_student'),
               ('查询学员信息','query_student'), ('显示所有学员信息','show_student_info'),
               ('退出','exit')]
    student_list = []
    def __init__(self):
        #存储数据所用的列表
        pass


    #1.程序入口函数，启动程序后执行不同功能
    @classmethod
    def run(cls):
        #加载学员信息
        cls.load_student()

        while True:
            # 显示菜单
            cls.show_menu()

            # 用户输入序号选择功能
            menu_num = int(input('请输入要选择的功能序号：'))

            # 根据用户输入的不同功能的序号选择功能
            if hasattr(cls,cls.opt_lst[menu_num-1][1]):
                getattr(cls,cls.opt_lst[menu_num-1][1])()

            else:
                print('还没有添加此功能------------！')


    @staticmethod
    def load_student():
        for student in Mypickle().load():
            StudentManager.student_list.append(student)
        print('学生信息加载完毕')


    @staticmethod
    def show_menu():
        for index,opt in enumerate(StudentManager.opt_lst,1):
            print(index,opt[0])

    @staticmethod
    def add_student():
        num = int(input('请输入要添加几名学员：'))
        count=0
        if num>0 and isinstance(num,int):
            while num>0:
                name = input('请输入要添加的学员的名字：')
                gender = input('请输入该学员的性别：')
                tel = input('请输入该学员的手机号码：')
                obj = Student(name,gender,tel)
                StudentManager.student_list.append(obj)
                num-=1
                count += 1
            opt = input('是否要保存到文件中（Y/N）：')
            if opt.upper()=='Y':
                for student in StudentManager.student_list[-count:]:
                    Mypickle().dump(student)
                print('学生信息保存完成')
            elif opt.upper()=='N':
                pass
        else:
            pass

    @staticmethod
    def delete_student():
        del_name=input('请输入要删除的学生的姓名：')
        del_tel = input('请输入要删除的学生的手机号码：')
        count=0
        for stu in StudentManager.student_list:
            if del_tel==stu.tel and del_name==stu.name:
                # print(count)
                # print(StudentManager.student_list)
                del StudentManager.student_list[count]
                # print(StudentManager.student_list)

                break
            else:
                count+=1
        opt = input('是否要保存操作到文件中（Y/N）：')
        if opt.upper() == 'Y':
            i = 0
            for student in StudentManager.student_list:
                if i==0:
                    Mypickle().del_dump(student)
                    i=1
                elif i==1 :
                    Mypickle().dump(student)
            print('学生信息保存完成')
        elif opt.upper() == 'N':
            pass

    @staticmethod
    def mod_student():
        name = input('请输入要修改的学生的姓名：')
        count=0
        for stu in StudentManager.student_list:
            if name==stu.name:
                gender = stu.gender
                tel = input('要修改成的手机号码：')
                del StudentManager.student_list[count]
                obj = Student(name,gender,tel)
                # Mypickle().dump(obj)
                StudentManager.student_list.append(obj)
                i = 0
                for student in StudentManager.student_list:
                    if i == 0:
                        Mypickle().del_dump(student)
                        i = 1
                    elif i == 1:
                        Mypickle().dump(student)
            else:
                count+=1

    @staticmethod
    def query_student():
        options = ['姓名','手机号码']
        for index,opt in enumerate(options,1):
            print(index,opt)
        ans = int(input('您想要按什么查找：'))
        if ans==1:
            name = input('请输入要查找的姓名:')
            for stu in StudentManager.student_list:
                if name==stu.name:
                    print("姓名：%s    性别：%s   手机号码：%s" % (stu.name, stu.gender, stu.tel))
                else:continue
        elif ans==2:
            tel = input('请输入要查找的手机号：')
            for stu in StudentManager.student_list:
                if tel==stu.tel:
                    print("姓名：%s    性别：%s   手机号码：%s" % (stu.name, stu.gender, stu.tel))
                else:continue

    @staticmethod
    def show_student_info():
        try:
            for student in Mypickle().load():
                print("姓名：%s    性别：%s   手机号码：%s" %(student.name,student.gender,student.tel))
        except:
            print('信息显示完毕～～～～')

    @staticmethod
    def exit():
        print('谢谢您的使用～～～')
        sys.exit()



if __name__ == '__main__':
    man = StudentManager()
    man.run()