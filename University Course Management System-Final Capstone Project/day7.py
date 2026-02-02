import random

print("1 = rock")
print("2 = paper")
print("3 = scissors")

try:
  user = int(input("Enter your choice:"))

  if user < 1 or user > 3:
    print("invalid input. Only 1,2,3 are allowed")

  else:  

    computer = ["rock", "paper", "scissors"]

    com_choice = random.choice(computer)

    if com_choice == "rock":
        if user == 1:
          print("tie")

        elif user == 2:
            print("you win")

        else:
            print("you lost")

    elif com_choice == "paper":
        if user == 1:
            print("you lost")

        elif user == 2:
            print("tie")     

        else:
            print("you win")


    elif com_choice == "scissors":
        if user == 1:
            print("you win")

        elif user == 2:
            print("you lost")    

        else:
            print("tie")   

  print(f"computer = {com_choice}")         
                                
except:
  print("invalid input. only values:1,2,3 are allowed")

