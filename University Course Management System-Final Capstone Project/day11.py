contact_list = {
    "ahad" : 4829157304,
    "hasbro" : 9371045862,
    "adam college" : 8124597036,
    "Isa Librarian" : 6714920583,
    "mikhail gorbachev" : 5867031249,
}
try:
    search = str(input("search contacts(Enter a name):"))

    print(contact_list[search])

except:
    print("No such contact found")    