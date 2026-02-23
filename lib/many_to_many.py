class Student:
    all =[]
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Student.all.append(self)

    def courses(self):
        return [schedule.course for schedule in Schedule.all if schedule.student == self]
    
    def calculate_gpa(self):
        grades = [schedule.grade for schedule in Schedule.all if schedule.student == self]
        return sum(grades) / len(grades)

class Course:
    all =[]
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        Course.all.append(self)    
        
    def students(self):
        return [schedule.student for schedule in Schedule.all if schedule.course == self]

class Schedule:
    all = []
    def __init__(self,student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
        Schedule.all.append(self)

    @property
    def student(self):
        return self._student
    
    @student.setter
    def student(self, value):
        if not isinstance(value, Student):
            raise Exception('Must be a student!')
        self._student = value

    @property
    def course(self):
        return self._course
    
    @course.setter
    def course(self, value):
        if not isinstance(value, Course):
            raise Exception
        self._course = value


student1 = Student('Hillary', 'Hillary@gmail.com')
student2 = Student('Gloria', 'Gloria@gmail.com')
student3 = Student('Ian', 'Ian@gmail.com')

course1 = Course('Physics', 'Mule')
course2 = Course('Nursing', 'Gladys')

Schedule(student2, course2, 100)
Schedule(student1, course1, 89)
Schedule(student3, course2, 49)
Schedule('Not student', course1, 40)

for course in student1.courses():
    print(course.title)

for students in Student.all:
    print(students.email)

for teacher in Course.all:
    print(teacher.teacher)

print(student1.calculate_gpa())

for student in course2.students():
    print(student.name)

