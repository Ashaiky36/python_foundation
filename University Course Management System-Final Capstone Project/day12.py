user = str(input("Enter a string:"))

tolist = list(user)

new_dic = {}
for val in tolist:
 new_dic[val] = new_dic.get(val, 0) + 1




print(new_dic) 