class Student:
    @staticmethod
    def grade_to_gpa(grade):
        if grade >= 90:
            return 4.0
        
        elif grade >= 80:
            return 3.0
        
        elif grade >= 70:
            return 2.0
        
        elif grade >= 60:
            return 1.0
        
        elif grade < 60:
            return 0.0
        
        else:
            return "Value error. Grade cannot be greater than 100"
        

gpa = Student.grade_to_gpa(85)   

print(f"The GPA for 85 is {gpa}")
        

        
       