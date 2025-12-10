
#fahrenheit to celsius converter func
def fahrenhiet_to_celsius(FtoC):
                return round(5/9 * (FtoC - 32), 2)

#pounds to kilogram converter func
def pound_to_kilo(PtoK):
                return round((PtoK *  0.45359237), 2)

#miles to kilometre converter func
def miles_to_km(MtoKM):
                return round((MtoKM * 1.609344), 2)

#main menu
print("Unit Converter")
print("Choose an option to access the specific converter:")
print("Fahrenheit to Celsius Converter: Enter 1")
print("Pound(lb) to Kilogram(kg) Converter: Enter 2")
print("Mile to Kilometer Converter: Enter 3")

while True:
    #user choice to navigate
    user_choice = int(input("Enter your choice:"))

    #proceed based on user choice
    if user_choice == 1:
        try:    
            FtoC = float(input("Enter temperation in fahrenhiet:"))
        
            
            print(f"{FtoC} fahrenhiet is {fahrenhiet_to_celsius(FtoC)} degree celsius" )
        except:
            print("Value Type Error. Converter only accepts float and integer values")    

    elif user_choice == 2:
        try:    
            PtoK = float(input("Enter weight in Pounds(lbs):"))
            
            print(f"{PtoK} pounds is {pound_to_kilo(PtoK)} kilograms")

        except:
            print("Value Type Error. Converter only accepts float and integer values")    


    elif user_choice == 3:
        try:    
            MtoKM = float(input("Enter distance in Miles:"))    
            
            print(f"{MtoKM} miles is {miles_to_km(MtoKM)} kilometres ")

        except:
            print("Value Type Error. Converter only accepts float and integer values")    
    #close the app and break the loop
    else:
        print("Closing application")
        break    
        