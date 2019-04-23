from core.person import Person
class Teacher(Person):pass
#     operate_lst=[('查看学生','show_student'),('查看班级','show_clas'),
#         ('查看课程','show_course')]
#     def show_student(self):
#         q1 = open('student_info', 'r')
#         r2 = q1.readlines()
#         print('欢迎查看学生账号：')
#         print(r2)
#         q1.close()
#     def show_course(self):
#         q2=open('course_info','rb')
#         while True:
#             try:
#                 course=pickle.load(q2)
#                 print(course)
#             except EOFError:
#                 break
#         q2.close()
#     def show_clas(self):
#         q3= open('clas_info','rb')
#         while True:
#             try:
#                 print(pickle.load(q3))
#             except EOFError:
#                 break
#         q3.close()