

new_items = str(input("Add a New Item:"))

grocery_list = []

grocery_list.append(new_items)

print(f"last item added:{grocery_list[-1]}")

print(f"grocery list:{grocery_list}")

remove_items = str(input("Enter the item you want to remove:"))
try:
    grocery_list.remove(remove_items)
except:
    print("Invalid input. you can only remove an item that is in the list")    

print(f"grocery list:{grocery_list}")

