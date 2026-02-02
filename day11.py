contact_list = {
    "ahad" : 4829157304,
    "hasbro" : 9371045862,
    "adam college" : 8124597036,
    "Isa Librarian" : 6714920583,
    "mikhail gorbachev" : 5867031249,
    "Ahad" : 4567890871
}

#simple method:
# try:
#     search = str(input("search contacts(Enter a name):"))

#     print(contact_list[search])

# except:
#     print("No such contact found")   
# 
# advance method: 

search = input("search contacts(Enter a name):")

result = contact_list.get(search, "contact not found")

if result == "contact not found" :
    print(f"{search}: not such contact exist")

else:
    print(f"""
contact name : {search}   
phone number : {result}

""")    