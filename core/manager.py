import hashlib
from conf import settings
from core.person import Person
from core.mypickle import MyPickle
from core.teacher import Teacher
class School:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
    def __repr__(self):
        s = ''
        for k in self.__dict__:
            s += '%s : %s | '%(k,self.__dict__[k])
        return s
class Clas:
    def __init__(self,num,clas_name,clas_course,clas_kind):
        self.num=num
        self.name=clas_name
        self.course=clas_course
        self.kind=clas_kind
    def __repr__(self):
        s = ''
        for k in self.__dict__:
            s += '%s : %s | '%(k,self.__dict__[k])
        return s
class Manager(Person):
    operate_lst = [
        ('创建学生账号','create_stu_id'),('创建老师账号','create_teach_id'),
        ('创建班级','create_clas'),('创建课程','create_course'),('创建学校', 'create_school'),
        ('查看学校', 'show_school'),('查看老师','show_teacher'),
        ('查看学生','show_student'),('查看班级','show_clas'),
        ('查看课程','show_course'),('退出','q')
    ]
    school_pickle = MyPickle(settings.school_pickle_path)
    clas_pickle=MyPickle(settings.clas_pickle_path)
    def create_stu_id(self):
        print('create_stu_id')
    def create_clas(self):
        num = input('班级人数：').strip()
        clas_name = input('班级名称：').strip()
        clas_couse = input('班级课程：').strip()
        clas_kind = input('班级性质：').strip()
        clas_obj = Clas(num, clas_name, clas_couse, clas_kind)
        Manager.clas_pickle.dump(clas_obj)
        print('创建班级成功！')
    def create_teach_id(self):
        # 用户输入用户名\密码
        # username = input('请输入要创建老师的姓名 : ')
        # passwd = input('请输入初始密码 : ')
        # # 密码进行摘要 盐是username
        # md5_obj = hashlib.md5(username.encode('utf-8'))
        # md5_obj.update(passwd.encode('utf-8'))
        # md5_passwd = md5_obj.hexdigest()
        # # 将新的用户名和密码,身份写入文件里
        # new_user_info = '%s|%s|%s\n' % (username, md5_passwd, 'Teacher')
        # with open(settings.userinfo,mode='a',encoding='utf-8') as f:
        #     f.write(new_user_info)
        # # 给老师选择一个校区
        # self.show_school()
        # school_num = int(input('请输入老师所在的校区序号 : '))
        # school_obj = self.school_pickle.get_item(school_num)
        # # 创建一个属于老师的新对象
        # teacher_obj = Teacher(username)
        # # 将老师选择的校区和老师对象绑定在一起
        # teacher_obj.school = school_obj
        # # 将老师对象整体dump进入teacherinfo文件
        # self.teacher_pickle.dump(teacher_obj)
        # # 显示老师创建成功
        print('创建老师成功!')
    def create_school(self):
        school_name = input('学校名称 : ')
        school_addr = input('学校地址 : ')
        school_obj = School(school_name,school_addr)
        Manager.school_pickle.dump(school_obj)
        print('创建学校成功！')
    def show_school(self):
        for num,i in enumerate(Manager.school_pickle.load(),1):
            print(num,i)
    def show_teacher(self):
        print('show_teacher')
    def show_student(self):
        print('show_student')
    def show_clas(self):
        for num,i in enumerate(Manager.clas_pickle.load(),1):
            print(num,i)
    def show_course(self):
        print('show_course')
    def create_course(self):
        print('create_course')

