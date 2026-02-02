# # simpler approach
# numbers = [1,2,3,4,5,6,7,8,9,10]

# numbers_sqaure = [ x**2 for x in numbers]

# print(numbers_sqaure)

# even_sqaures = [val for val in numbers_sqaure if val % 2 == 0]

# print(even_sqaures)


#advanced approach

numbers = [1,2,3,4,5,6,7,8,9,10]

even_sqaures  = [x**2 for x in numbers if (x**2)%2==0]

print(even_sqaures)
