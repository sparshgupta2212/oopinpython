from src.Student import Student
roll=eval(input("enter the roll number"))
name=input("enter name")
marks=eval(input("enter the marks"))
bhatiaji=Student(roll,name,marks)
print(bhatiaji.cpi)
a=Student()
a1=Student()
print(Student.count)
print(Student.stat_method())