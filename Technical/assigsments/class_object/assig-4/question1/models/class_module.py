class Student:
    def __init__(self,rno,sname,smarks):
         self.roll_no=rno
         self.student_name=sname
         self.marks=smarks
    @classmethod
    def display_Student(cls,student_list):
         for student in student_list:
             print(f"{student.student_name , student.roll_no,student.marks}")
    @classmethod
    def display_Student_greter_60(cls,student_list):
         for student in student_list:
             if student.marks>60:
                    print(f"{student.student_name , student.roll_no,student.marks}")
    @classmethod
    def highest_marks_student(cls,student_list):
         maxmark=student_list[0].marks
         st=0
         for student in student_list:
             if student.marks>maxmark:
                    st=student
         student=st
         print(f"{student.student_name , student.roll_no,student.marks}")
    @classmethod
    def average_marks_of_Student(cls,student_list):
         sum=0
         for student in student_list:
             sum+=student.marks
         return sum/len(student_list)

  
 
         
         
         
