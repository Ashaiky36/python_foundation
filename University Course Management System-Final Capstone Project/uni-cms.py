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
    def save_data(filename):
         data = {}
         try:
            with open (filename, 'w', encoding="utf-8") as file:
              json.dump(data, file, ensure_ascii=False, indent=4)

            print("database updated successfully")  
            
            
            
         except:
             print("file does not exists")    


# print("University Course Management System")
# print("----------start screen-------------")

# u_id = str(input("Enter your unique user id:"))

# def verify_user(u_id, filepath = "users.json"):
#     filepath = "users.json"
#     with open(filepath, 'r') as file:
#         data = json.load(file)
#         for i in data:
#             if i["id"] == u_id:
#                 return True   

user_id = str(input("Enter your unique user id:"))
                                
class User:
    def __init__(self, user_id, username, role):
        self.user_id = user_id
        self.username = username
        self.role = role

    def login(self):
        users = DataHandler.load_data("users.json")

        for user in users:
            if user["id"] == user_id:
                print("user exists. login successful")
                if user["role"] == "admin":
                    class Admin(User):
                        c_id = str(input("Enter a unique id for the course:"))
                        c_name = str(input("Enter the course name:"))
                        instructor = str(input("Enter the instructor name foe the course:"))
                        capacity = int(input("Enter student capacity for this course:"))
                        def create_course(self, c_id, c_name, instructor, capacity):
                            self.c_id = c_id
                            self.c_name = c_name
                            self.instructor = instructor
                            self.capacity = capacity

                else:
                    class Student(User):
                        print("checking...........")     


User.login(user_id)                                        