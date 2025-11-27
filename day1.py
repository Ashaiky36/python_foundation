name = input("Enter your name:")

try:

  age = int(input("Enter your age:"))

  new_age = age+5

  print(f"In 5 years, {name} would be {new_age}")

except:
    print("age should be an integer")
     


