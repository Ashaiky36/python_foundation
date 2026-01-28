import json
import os

class DataHandler:
    @staticmethod
    def load_data(filename):
        try:
            
            with open(filename, 'r') as file:
               data = json.load(file)  
               return data   

        except:
            print("file does not exists")   

    @staticmethod
    def save_data(filename, courses):
         try:
            with open (filename, 'w', encoding="utf-8") as file:
              json.dump(courses, file, ensure_ascii=False, indent=4)

            print("database updated successfully")  
            
            
            
         except:
             print("file does not exists")    


print("University Course Management System")
print("----------start screen-------------")
print("enter your user id to login and access role specific features")


user_id = str(input("Enter your unique user id:"))
                                
class User:
    def __init__(self, user_id, username = None, role = None):
        self.user_id = user_id
        self.username = username
        self.role = role

    def login(self):
        users = DataHandler.load_data("users.json")

        for user in users:
            if user["id"] == user_id:
                print("login successful")
                if user["role"] == "admin":
                    print("""
admin features:
create course = enter 1
delete course = enter 2
view all courses = enter 3
exit = enter 4""")
                   
                    class Admin(User):
                        # c_id = str(input("Enter a unique id for the course:"))
                        # c_name = str(input("Enter the course name:"))
                        # instructor = str(input("Enter the instructor name foe the course:"))
                        # capacity = int(input("Enter student capacity for this course:"))
                        def __init__(self, c_id = None, c_name = None, instructor = None, capacity = None):
                            self.c_id = c_id
                            self.c_name = c_name
                            self.instructor = instructor
                            self.capacity = capacity

                        def create_course(self):
                            new_course = {}

                            new_course["id"] = self.c_id
                            new_course["name"] = self.c_name
                            new_course["instructor"] = self.instructor
                            new_course["capacity"] = self.capacity

                            print(new_course)

                            courses = DataHandler.load_data("courses.json")
                            courses.append(new_course)

                            DataHandler.save_data("courses.json", courses)

                        def delete_course(self):
                            course_list = DataHandler.load_data("courses.json")
                            new_course_list = [course for course in course_list if course.get("id") != self.c_id]

                            DataHandler.save_data("courses.json", new_course_list)
                            # for course in course_list:
                            #     if course["id"] == self.c_id:
                            #         new_list = course_list.remove(course)
                            #         break
                            # DataHandler.save_data("courses.json", new_list)        
                        
                        def view_all_courses(self):
                            course_list = DataHandler.load_data("courses.json")
                            print(course_list)

                    while True:
                        
                         admin_option = int(input("select feature:"))
                         if admin_option == 1:
                                c_id = str(input("course id:"))
                                c_name = str(input("course name:"))        
                                c_instructor = str(input("course's instructor name:"))
                                c_capacity = int(input("maximum course capacity:"))
                                acc_1 = Admin(c_id, c_name, c_instructor, c_capacity)       
                                acc_1.create_course() 

                         elif admin_option == 2:
                                course_to_delete = str(input("course id of the course you want to delete:")) 
                                adc_1 = Admin(course_to_delete)
                                adc_1.delete_course()

                         elif admin_option == 3:
                                vac_1 = Admin()
                                vac_1.view_all_courses()

                         elif admin_option == 4:
                             print("logging off......")
                             print("exiting......")  
                             break     

                         else:
                                print("enter a valid option")           


                elif user["role"] == "student":
                    print("""
student features:
view all courses = enter 1
enroll in a course = enter 2
view schedule = enter 3
exit = enter 4""")
                    class Student(User):
                        def __init__(self, c_id = None):
                            self.c_id = c_id
                            super().__init__(user_id)
                            
                        def view_all_courses(self):
                            course_list = DataHandler.load_data("courses.json")
                            print(course_list)

                        def enroll_in_course(self):
                            courses = DataHandler.load_data("courses.json")
                            enrollments = DataHandler.load_data("enrollments.json")
                            count = sum( self.c_id in course_list for course_list in enrollments.values())
                            for course in courses:
                                if course["id"] == self.c_id:
                                    capacity = course["capacity"]
                                    if count < capacity:
                                        for course in courses:
                                            if course["id"] == self.c_id:
                                                if user_id in enrollments:
                                                    enrollments[user_id].append(self.c_id)
                                                else: 
                                                    enrollments[user_id] = [self.c_id]    
                                                    # enrollments.setdefault(user_id, [].append([self.c_id]))
                                                DataHandler.save_data("enrollments.json", enrollments)
                                                break
                                    else:
                                        print("course is full")        

                            
                                    #need to implement course capacity limit           
                        def view_schedule(self):
                            schedule = DataHandler.load_data("enrollments.json")
                            schedule_details = DataHandler.load_data("courses.json")
                            if user_id in schedule:
                                for course_id in schedule[user_id]:
                                    for course in schedule_details:
                                        if course["id"] == course_id:
                                            print(f"{course["id"]}, {course["name"]} , {course["instructor"]}") 

                    while True:
                        student_option = int(input("select feature:"))    
                        if student_option == 1:
                            vac_2 = Student()
                            vac_2.view_all_courses()  

                        elif student_option == 2:
                            course_id = str(input("enter course id:"))    
                            eic_1 = Student(course_id)       
                            eic_1.enroll_in_course()

                        elif student_option == 3:
                            vs_1 = Student()
                            vs_1.view_schedule()

                        elif student_option == 4:
                             print("logging off......")
                             print("exiting......")  
                             break     

                        else:
                                print("enter a valid option")                         

                   




User.login(user_id)   

# class Course: