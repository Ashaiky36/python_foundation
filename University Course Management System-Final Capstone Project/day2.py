
try:
    
  weight = float(input("Enter your weight in kg:"))
  try:
    check = 10/weight

  except ZeroDivisionError:
    print("weight cannot be zero")  

  height = float(input("Enter your height in meters:"))

  bmi = weight / (height * height)

  print(f"your BMI is:{bmi:.2f}")

except ValueError:
  print("error: invalid input. only stick to float values(eg. 70.2kg, 1.63m)") 

except ZeroDivisionError:
  print("height cannot be zero")