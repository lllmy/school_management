from core.person import Person
class Student(Person):pass
#     operate_lst=[('查看老师', 'show_teacher'), ('查看班级', 'show_clas'),
#         ('查看课程', 'show_course'),
#     ]
#     def show_teacher(self):
#         t1=open('teacher_info','r')
#         r3=t1.readlines()
#         print('欢迎查看老师账号：')
#         print(r3)
#         t1.close()
#     def show_course(self):
#         t2 = open('course_info', 'rb')
#         while True:
#             try:
#                 course = pickle.load(t2)
#                 print(course)
#             except EOFError:
#                 break
#         t2.close()
#     def show_clas(self):
#         t3 = open('clas_info','rb')
#         while True:
#             try:
#                 print(pickle.load(t3))
#             except EOFError:
#                 break
#         t3.close()