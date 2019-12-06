class Student:
    count=0

    #every non static method includes self as the first parameter
    def __init__(self,roll_number=0,name='',marks=0.0):
        self.roll_number=roll_number
        self.name=name;
        self.marks=marks;
        self.cpi=self.calculate_cpi(self.marks)
        Student.count=Student.count+1;
    def calculate_cpi(self,marks):
        if 100<=marks<=91:
            return 10.0
        elif 90<=marks<=81:
            return 9.0
        else :
            return 8.0
    @staticmethod
    def stat_method():
        print("static method")
    def __str__(self):
        return self.name,self.cpi
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
