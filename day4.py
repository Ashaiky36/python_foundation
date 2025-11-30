#grade calculator

try:
    marks = int(input("Enter your marks(1-100):"))
    if marks>=0 and marks<=100:    
        


        if marks >= 80:
            print(f"{marks} = Grade A")

        elif marks >= 60:
            print(f"{marks} = Grade B")  

        elif marks >= 40:
            print(f"{marks} = Grade C")

        elif marks >= 20:
            print(f"{marks} = Grade D") 

        else:
            print("Grade F")

    else:
        print("Enter an integer only between 1-100")          

except:
    print("Enter an Integer")