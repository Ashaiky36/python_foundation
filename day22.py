#student's average grade calculator

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        

    def get_avg(self):
        total = sum(self.grades)
        total_sub = len(self.grades)
        avg = round((total/total_sub), 2)
        print(f"{self.name} has an average grade of {avg}")

S1 = Student("Ahad", [56,78,89,60,91,98])   
S2 = Student("Haseeb", [67, 72, 78, 84, 89, 90])
S3 = Student("Zohara", [72, 76, 84, 91, 95, 97])

S1.get_avg()
S2.get_avg()
S3.get_avg()

