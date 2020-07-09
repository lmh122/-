'''
存储数据的位置：文件（student.data）
加载文件数据
修改数据后保存文件

存储数据的形式：列表存储学员对象

系统功能：

添加学员
删除学员
修改学员
查询学员信息
显示所有学员信息
保存学员信息

'''

class StudentManager(object):
    opt_lst = [('添加学员','add_student'), ('删除学员','delete_student'), ('修改学员','mod_student'),
               ('查询学员信息','query_student'), ('显示所有学员信息','show_student_info'),
               ('保存学员信息','save_student_info'),
               ('退出','exit')]
    def __init__(self):
        #存储数据所用的列表
        self.student_list=[]


    #1.程序入口函数，启动程序后执行不同功能
    @classmethod
    def run(cls,ret):
        #加载学员信息
        ret.load_student()

        while True:
            # 显示菜单
            cls.show_menu()

            # 用户输入序号选择功能
            menu_num = int(input('请输入要选择的功能序号：'))

            # 根据用户输入的不同功能的序号选择功能
            if hasattr(ret,cls.opt_lst[menu_num-1][1]):
                getattr(ret,cls.opt_lst[menu_num-1][1])()

            else:
                print('还没有添加此功能------------！')



    def load_student(self):
        pass

    @staticmethod
    def show_menu():
        for index,opt in enumerate(StudentManager.opt_lst,1):
            print(index,opt[0])


    def add_student(self):
        print('增加')


    def delete_student(self):
        pass


    def mod_student(self):
        pass


    def query_student(self):
        pass


    def show_student_info(self):
        pass

    def save_student_info(self):
        pass


    def exit(self):
        pass



manager = StudentManager()

