#age in days calculator using python datetime module
from datetime import date, datetime


today = date.today()
print(today)
try:
    bday = str(input("Enter your DOB(YYYY-MM-DD):"))

    user_bday = datetime.strptime(bday, "%Y-%m-%d").date()

    num_days = (today - user_bday).days

    print(f"you have lived for {num_days} days")

except:
    print("Format error. Enter your date of birth in specified format")    
