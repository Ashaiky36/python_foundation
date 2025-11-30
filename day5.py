#version one using while loop
# try:
 
#   start = int(input("enter an integer:"))

#   if start > 0:

#         i = 1

#         while i<=10:
#             print(start * i)

#             i+=1
#   else:
#         print("enter a positive integer!")  

# except:              
#     print("Enter an integer only")


##########################################
#version two- using for loop and ranges()--prefered
try:
    start = int(input("Enter an integer:"))
    if start>0:

        stop = start * 11

        step = start

        for x in range(1, 11):
            answer = start * x
            print(f"{start} * {x} = {answer}")
    else:
        print("Enter a postive integer!") 
except:
    print("Enter an integer only!")                   
