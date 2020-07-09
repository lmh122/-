
'''
学员信息包含：姓名，性别，手机号
添加__str__方法，方便查看学员对象信息

'''


class Student(object):
    def __init__(self,name,gender,tel):
        self.name = name
        self.gender = gender
        self.tel = tel


    def __str__(self):
        return '%s,%s,%s' %(self.name,self.gender,self.tel)



# lmh = Student('lmh','男','xxxxxxxxxxxx')
# print(lmh)