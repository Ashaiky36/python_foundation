#try, except, else and special ValueError, ZeroDivisionError errors
while True:
    try:
        nume = float(input("Enter a numerator:"))
        deno = float(input("Enter a denominator:"))

        division = round((nume/deno), 2)

    except ValueError:
        print("Value Error. Input is not a number")

    except ZeroDivisionError:
        print("Zero Division Error. Denominator cannot be zero")

    else:
        print(f"answer = {division}")     
        break       