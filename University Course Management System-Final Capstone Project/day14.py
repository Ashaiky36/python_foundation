#todo manager
print("Welcome to TO-DO Manager!")
print("Enter 1: Add a new task")
print("Enter 2: View a existing task")
print("Enter 3: Mark a task as done")
print("Enter 4: Delete a task")
print("Enter 5: To exit")

todo_list = []

while True:
    user = int(input("Enter a number:"))

    if user == 1:
        t_add = str(input("Enter a new task:"))
        try:
            new_id = todo_list[-1]['id'] + 1 if todo_list else 1
            new_t = {"id": new_id, "task": t_add, "status": "Pending"}
            todo_list.append(new_t)
            print("Task added successfully:")
            print(todo_list)
        except:
            print("new task cannot be empty")    

    elif user == 2:
        t_view = str(input("Enter a task name to view:"))
        try:
            t_view_rest = [item for item in todo_list if item.get("task") == t_view]
            print(t_view_rest)
            
        except:
            print("No such task exist")    

    elif user == 3:
        t_mark = str(input("Enter the task to mark it as done:"))
        found = False
        for item in todo_list:
            if item["task"] == t_mark:
                item["status"] = "completed"  
                print(todo_list)
                print(f"task : {t_mark} marked done")
                found = True
                break
            else:
                print("entered task name does not match any tasks in database")     

    elif user == 4:
        t_del = str(input("Enter the task you want to delete:"))
        # for item in todo_list:
        #     if item["task"] == t_del:
        #         todo_list.remove(item)
        #         print(todo_list)
        #     else:
        #         print("The task you are trying to delete does not exist in the database") 
        t_del_list = [item for item in todo_list if item.get("task") != t_del]

        if len(t_del_list) < len(todo_list):
            todo_list = t_del_list
            print(todo_list)
            print(f"task : {t_del} is removed successfully")

        else:
            print("Value error. No such task exist in the database")   
        
           

    else:
        print("closing app")      
        break    
    