#student's average grade calculator with usage of dunder method of __str_

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        

    def __str__(self):
        total = sum(self.grades)
        total_sub = len(self.grades)
        avg = round((total/total_sub), 2)
        return f"Student name = {self.name}, average = {avg}"

        

S1 = Student("Ahad", [56,78,89,60,91,98])   
S2 = Student("Haseeb", [67, 72, 78, 84, 89, 90])
S3 = Student("Zohara", [72, 76, 84, 91, 95, 97])

print(str(S1))
print(S2)
print(str(S3))

